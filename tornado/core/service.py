#!/usr/bin/python
# -*- coding: utf-8 -*-

import traceback

from core import dbmysql
from core.err_code import OCT_SYSTEM_ERR
from core.log import ERROR
from modules.api.api_web import web_add_apiresult


def web_get_env(session):
	env = {
		"USERNAME": session.get("user"),
		"SESSIONID": session.get("id"),
	}

	if (session.get("cookie")):
		env["ROLE"] = session["cookie"].get("role")
		env["USERID"] = session["cookie"].get("id")

	return env


def makeFunctionResult(funret):
	RetCode = funret.get('RetCode')
	if type(RetCode) != int:
		errorLog = "Wrong formatstr in function return data ret[%s]" % (funret)
		ERROR(errorLog)
		return buildResult(OCT_SYSTEM_ERR, errorLog=errorLog)

	return buildResult(RetCode, funret.get("RetObj"), funret.get("ErrorLog"))


def writeApiWithResult(db, env, arg, result, apiProto, server=False):
	if arg["api"].split(".")[3] == "task":
		return result

	if (apiProto.get("isTask")):
		result["apiId"] = result["RetObj"]
	else:
		retObj = web_add_apiresult(db, env, arg, result)
		result["apiId"] = retObj["RetObj"]["id"]

	return result


def callWebServiceEX(*args):
	function = args[-4]
	session = args[-3]
	arg = args[-2]
	apiProto = args[-1]

	if (apiProto):
		arg["apiName"] = apiProto["name"]

	env = web_get_env(session)
	db = dbmysql.mysqldb()

	try:
		funret = function(db, env, arg)
	except Exception as e:
		errorLog = "Error in %s: [%s],\n Import module failed. [%s]" % (function, e, traceback.format_exc(limit=100))
		errorLog = errorLog.replace("\n", "")
		errorLog = errorLog.replace("\"", "\\\"")
		ERROR(errorLog)

		retObj = buildResult(OCT_SYSTEM_ERR, errorLog=errorLog)
		if (arg.get("async") != True):
			retObj = writeApiWithResult(db, env, arg, retObj, apiProto, False)
			retObj["session"] = session

		del db, env
		return retObj

	retObj = makeFunctionResult(funret)
	if (arg.get("async") != True):
		retObj = writeApiWithResult(db, env, arg, retObj, apiProto, False)
		retObj["session"] = session
	del db, env

	return retObj


def buildResult(RetCode, data=None, errorLog=""):
	return {
		"RetObj": data,
		"RetCode": RetCode,
		"ErrorLog": errorLog
	}


def callWebServiceDir(function, session, args, apiProto):
	return callWebServiceEX(function, session, args, apiProto)

#!/usr/bin/python
# -*- coding: utf-8 -*-


import json
import sys
import traceback

from core import dbmysql
from core.err_code import NO_AUTH_SKEY, UNACCP_PARAS, SYSCALL_ERR
from core.log import ERROR, DEBUG, INFO
from models.Common import DEFAULT_ACCOUNT_ID
from utils.commonUtil import getUuid, isSystemWindows
from utils.httpUtil import buildReply, getArgObj, buildFailureReply, appendBaseArg
from utils.sessionUtil import getSession
from views.api.dispatch import doDispatching, IGNORE_SESSION_APIS

sys.path.append("../")

import tornado
import tornado.httpclient
import tornado.ioloop
import tornado.web
import tornado.gen
import tornado.websocket
import tornado.options
from conf.config import *
from views.api.center.api import API_MODULE_LIST, API_PREFIX, PARAM_TYPE_INT

LISTEN_PORT = 8080
LISTEN_ADDR = "0.0.0.0"

API_PROTOS = {}
API_VIEW_LIST = {}

TEMPLATE_NOT_FOUND = "pagenotfound.html"
TEMPLATE_ROBOT = "robot.html"
TEMPLATE_DASHBOARD = "dashboard.html"
TEMPLATE_CONFIG = "config.html"

TEMPLATE_LIST = {
	"index": TEMPLATE_DASHBOARD,
	"robot": TEMPLATE_ROBOT,
	"config": TEMPLATE_CONFIG,
}


def getTemplate(module="index"):
	return TEMPLATE_LIST.get(module) or (TEMPLATE_NOT_FOUND)


class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/", MainHandler),
			(r"/ui/", MainHandler),
			(r"/ui/(.*)/", MainHandler),
			(r"/ui/(.*)/(.*)/", MainHandler),
			(r"/api/", ApiHandler),
			(r"/api/test/", ApiTestHandler),
			(r"/files/upload/", FileUploadHandler),
		]
		settings = dict(
			cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
			template_path=os.path.join(os.path.dirname(__file__), "templates"),
			static_path=os.path.join(os.path.dirname(__file__), "static"),
			xsrf_cookies=False,
		)
		tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	@tornado.gen.coroutine
	def get(self, module="index", action=None):
		templatePath = getTemplate(module)
		if (not templatePath):
			self.render(TEMPLATE_NOT_FOUND)
		else:
			self.render(templatePath)


class ApiTestHandler(tornado.web.RequestHandler):
	result = {
		"moduleSelected": "account",
		"apiSelected": "octlink.wcrobot.v1.account.APILoginByAccount",
		"request": "{}",
		"reply": "{}",
		"paras": "{}"
	}

	@tornado.web.asynchronous
	def get(self):

		self.render("testapi.html", moduleList=API_VIEW_LIST,
		            moduleListStr=json.dumps(API_VIEW_LIST, indent=4),
		            result=self.result,
		            resultStr=json.dumps(self.result, indent=4, ensure_ascii=False))

	@tornado.web.asynchronous
	@tornado.gen.coroutine
	def post(self, *args, **kwargs):

		argObj = getArgObj(self.request)
		api = argObj["api"]
		paras = argObj["paras"]
		async = False

		if paras["timeout"] != 0:
			async = True

		api_body = {
			"api": api,
			"paras": paras,
			"async": async,
			"session": {
				"uuid": "00000000000000000000000000000000"
			}
		}

		self.result["paras"] = argObj["paras"]
		self.result["moduleSelected"] = argObj["module"]
		self.result["apiSelected"] = argObj["api"]
		self.result["request"] = json.dumps(argObj, indent=4, ensure_ascii=False)

		client = tornado.httpclient.AsyncHTTPClient()

		url = "http://%s:%d/api/" % ("127.0.0.1", RUNNING_PORT)
		ERROR("%sfff" % url)
		response = yield client.fetch(url, method="POST", request_timeout=10, connect_timeout=10,
		                              body=json.dumps(api_body))
		self.on_response(response)

	def on_response(self, resp):

		body = json.loads(str(resp.body, encoding="utf-8"))
		if body == None:
			result = buildFailureReply(SYSCALL_ERR)
			self.result["reply"] = json.dumps(result, indent=4, ensure_ascii=False)
			self.write(json.dumps(result, indent=4, ensure_ascii=False))
		else:
			self.result["reply"] = json.dumps(body, indent=4, ensure_ascii=False)
			self.write(body)

		self.redirect("/api/test/")


def getSessionId(argObj):
	session = argObj.get("session")
	if (session):
		return session.get("uuid")
	else:
		return None


UPLOAD_API_MAP = {
	"APISystemUpgrade": "octlink.center.v5.upgrade.APISystemUpgrade",
	"APIUploadLicense": "octlink.center.v5.license.APIUploadLicense"
}


class FileUploadHandler(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	@tornado.gen.coroutine
	def post(self):

		self.db = dbmysql.mysqldb()

		if isSystemWindows():
			filePath = "var/tmp/" + getUuid()
		else:
			filePath = "/tmp/" + getUuid()

		# get the request file to cache path
		try:
			file_metas = self.request.files['file']
		except:
			file_metas = self.request.files['filename']

		for meta in file_metas:
			with open(filePath, 'wb') as up:
				up.write(meta['body'])

		argObj = appendBaseArg({}, self.request)
		argObj["paras"]["role"] = 7
		argObj["paras"]["accountId"] = DEFAULT_ACCOUNT_ID

		api_key = self.get_argument("api", None)
		if (not api_key):
			self.write(buildFailureReply(UNACCP_PARAS, errorMsg="api key error"))
			self.finish()
			return

		argObj["paras"]["filePath"] = filePath
		argObj["api"] = UPLOAD_API_MAP.get(api_key)
		if (not argObj["api"]):
			self.write(buildFailureReply(UNACCP_PARAS, errorMsg=api_key))
			self.finish()
			return

		session = getSession(self.db, sessionId="00000000000000000000000000000000")

		argObj["session"] = session
		retObj = doDispatching(argObj, session, API_PROTOS)
		self.write(buildReply(retObj))
		self.finish()


class ApiHandler(tornado.web.RequestHandler):
	SUPPORTED_METHODS = ("POST")

	db = None

	def __init__(self, application, request, **kwargs):
		super(ApiHandler, self).__init__(application, request, **kwargs)

		self.db = dbmysql.mysqldb()

	def checkSession(self, argObj):
		apiName = argObj.get("api")

		if (apiName.split(".")[-1] in IGNORE_SESSION_APIS):
			DEBUG("User login API, no need check session")
			return (True, {})

		sessionId = getSessionId(argObj)
		if (not sessionId):
			return (False, {})

		DEBUG("got session id %s" % sessionId)

		sessionObj = getSession(self.db, sessionId)
		if not sessionObj:
			return (False, {})

		return (True, sessionObj)

	def getAccountInfo(self, session):

		if session.get("cookie"):
			role = session["cookie"]["role"] or 7
			accountId = session["cookie"]["id"] or DEFAULT_ACCOUNT_ID
		else:
			role = 7
			accountId = DEFAULT_ACCOUNT_ID

		return role, accountId

	@tornado.web.asynchronous
	def post(self, *args, **kwargs):
		argObj = getArgObj(self.request)

		# import time
		# yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time() + 10)

		if (not argObj.get("api")):
			ERROR("not a valid api, no api exist")
			self.write(buildFailureReply(UNACCP_PARAS))
			self.finish()
			return

		(status, session) = self.checkSession(argObj)
		if (not status):
			ERROR("check session failed %s " % str(argObj))
			self.write(buildFailureReply(NO_AUTH_SKEY))
			self.finish()
			return

		(role, accountId) = self.getAccountInfo(session)
		argObj["paras"]["role"] = role

		# IF accountId Specified, just use it
		if not argObj["paras"].get("accountId"):
			argObj["paras"]["accountId"] = accountId

		retObj = doDispatching(argObj, session, API_PROTOS)
		self.write(buildReply(retObj))
		self.finish()


def runWebServer(addr, port):
	tornado.options.parse_command_line()
	app = Application()
	app.listen(port, addr)
	tornado.ioloop.IOLoop.instance().start()


def loadFunction(apiProto):
	serviceName = apiProto["serviceName"]
	if (not serviceName):
		apiProto["func"] = None
		return True

	funcName = serviceName.split(".")[-1]
	modulePath = serviceName.split(".")[:-1]

	try:
		service = __import__("modules." + ".".join(modulePath), fromlist=["from modules import"])
	except Exception as e:
		print(('Import module failed. [%s]' % funcName))
		print(('Import module failed. [%s]' % e))
		print(('Import module failed. [%s]' % traceback.format_exc()))
		return False

	if hasattr(service, funcName):
		funcObj = getattr(service, funcName)
		apiProto["func"] = funcObj
	else:
		print(('There is no %s in %s' % (funcName, modulePath)))
		del service
		return False

	return True


def loadAPIs():
	global API_PROTOS

	for moduleName in API_MODULE_LIST:
		module = __import__("views.api.center.api_" + moduleName, fromlist=["from views import"])
		for (k, v) in list(module.funcList.items()):
			key = API_PREFIX + "." + moduleName + "." + k
			if (not loadFunction(v)):
				print("load function error")
				return False
			API_PROTOS[key] = v

	print("Loaded all APIs OK!")

	return True


def loadViewAPIs():
	def copy_paras(paras):

		copyed_paras = {}
		for (k, v) in list(paras.items()):
			copyed_paras[k] = v

		append_extra_paras(copyed_paras)

		return copyed_paras

	def append_extra_paras(paras):

		if (not paras.get("paras")):
			paras["timeout"] = {
				"default": 0,
				"type": PARAM_TYPE_INT,
				"desc": "Timeout Value",
				"descCN": "超时时间，0表示同步调用",
			}

	global API_VIEW_LIST

	for moduleName in API_MODULE_LIST:

		API_VIEW_LIST[moduleName] = []

		module = __import__("views.api.center.api_" + moduleName, fromlist=["from views import"])
		for (k, v) in list(module.funcList.items()):
			key = API_PREFIX + "." + moduleName + "." + k
			apiProto = {
				"name": v["name"],
				"key": key,
				"paras": copy_paras(v.get("paras") or {})
			}
			API_VIEW_LIST[moduleName].append(apiProto)

	print("Loaded all APIs OK!")


def init():
	if (not loadAPIs()):
		return False

	loadViewAPIs()

	return True


# def startApiEngine():
#	_thread.start_new_thread(apiEngine, ("API Engine Thread", 20))


if __name__ == "__main__":

	if (float(tornado.version.split(".")[0]) < 3.0):
		print(("Version of tornado [%s] is too low, we need 3.0 above" % (tornado.version)))
		sys.exit(1)

	if (not init()):
		print("init Center API Engine Failed")
		exit(1)

	if (len(sys.argv) != 3):
		addr = LISTEN_ADDR
		port = LISTEN_PORT
	else:
		addr = sys.argv[1]
		port = int(sys.argv[2])

	global RUNNING_PORT

	RUNNING_PORT = port

	print("To start to run webServer in %s:%d" % (addr, port))

	INFO("To start to run webServer in %s:%d" % (addr, port))

	runWebServer(addr, port)

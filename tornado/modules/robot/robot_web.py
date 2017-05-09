#!usr/bin/python
# -*- coding: utf-8 -*- 

from core.err_code import OCT_SUCCESS, USER_PASSWD_ERR, USER_NOT_EXIST
from modules.robot import robot as robotService
from utils.commonUtil import buildRetObj


def web_get_robot(db, env, arg):
	ret, data = robotService.get_robot(db, arg["paras"]["id"])
	return buildRetObj(ret, data)


def web_get_allrobot(db, env, arg):
	ret, data = robotService.get_allrobot(db, arg)
	return buildRetObj(ret, data)


def web_get_robotlist(db, env, arg):
	(ret, data) = robotService.get_robotlist(db)
	return buildRetObj(ret, data)


def web_add_robot(db, env, arg):
	ret = robotService.add_robot(db, arg)
	return buildRetObj(ret)


def web_del_robot(db, env, arg):
	ret = robotService.delete_robot(db, arg["paras"]["id"])
	return buildRetObj(ret)


def web_login(db, env, arg):
	return buildRetObj(OCT_SUCCESS)


def web_logout(db, env, arg):
	return buildRetObj(OCT_SUCCESS)


def web_update_robot(db, env, arg):
	ret = robotService.update_robot(db, arg)
	return buildRetObj(ret)
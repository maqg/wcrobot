#!usr/bin/python
# -*- coding: utf-8 -*- 

from core import dbmysql
from core.err_code import USER_ALREADY_EXIST, USER_NOT_EXIST
from models.Robot import *


AUTHKEY_TIMEOUT = 24 * 30 * 60

def get_robotlist(db, arg):

	robot_list = []

	cond = "WHERE 1=1 "
	cond += "AND R_AccountId='%s' " % arg["paras"]["accountId"]

	ret = db.select(TB_ROBOT, cond="")
	if ret == -1:
		ERROR("get robot list error")
		return (DB_ERR, None)

	for dur in db.cur:
		obj = dbmysql.row_to_dict(TB_ROBOT, dur)
		temp = {
			"id": obj["ID"],
			"name": obj["R_Name"],
		}
		robot_list.append(temp)

	DEBUG(robot_list)

	return (OCT_SUCCESS, robot_list)


def get_allrobot(db, arg):

	listObj = {
		"total": 0,
		"robots": [],
	}

	start = arg["paras"].get("start") or 0
	limit = arg["paras"].get("limit") or 100

	cond = "WHERE 1=1 "
	cond += "AND R_AccountId='%s' " % arg["paras"]["accountId"]

	ret = db.select(TB_ROBOT, cond=cond, limit=int(limit), offset=int(start))
	if ret == -1:
		ERROR("get robot list error")
		return (DB_ERR, None)

	for dur in db.cur:
		obj = dbmysql.row_to_dict(TB_ROBOT, dur)
		robot = WCRobot(db, dbObj=obj)
		robot.loadFromObj()

		listObj["robots"].append(robot.toObj())

	listObj["total"] = getRobotCount(db, cond=cond)

	return (OCT_SUCCESS, listObj)


def get_robot(db, robotId):
	robot = WCRobot(db, robotId)

	if (robot.init() != 0):
		ERROR("robot %s not exist" % robotId)
		return (USER_NOT_EXIST, None)

	return (OCT_SUCCESS, robot.toObj())


def add_robot(db, env, arg):

	paras = arg["paras"]
	robotName = paras["name"]

	robot = getRobot_byName(db, robotName)
	if (robot):
		WARNING("robot %s already exist" % robotName)
		return USER_ALREADY_EXIST

	robot = WCRobot(db)

	robot.name = robotName
	robot.phone = paras.get("phoneNumber") or ""
	robot.uId = paras.get("uId") or ""
	robot.accountId = paras.get("accountId")

	return robot.add()


def delete_robot(db, arg):

	robotId = arg["paras"]["id"]
	robot = getRobot(db, robotId)
	if (not robot):
		ERROR("account %s not exist" % (robotId))
		return USER_NOT_EXIST

	return robot.delete()


def update_robot(db, arg):

	paras = arg["paras"]
	robotId = paras["id"]

	robot = getRobot(db, robotId)
	if (not robot):
		ERROR("robot %s not exist" % (robotId))
		return USER_NOT_EXIST

	robot.uId = paras["uId"]
	robot.name = paras["name"]

	return robot.update()
#!/usr/bin/python
# -*- coding: utf-8 -*-

from conf.dbconfig import TB_ROBOT
from core.err_code import DB_ERR, OCT_SUCCESS, NOT_ENOUGH_PARAS
from core.log import DEBUG, ERROR, WARNING
from models.Common import DEFAULT_ACCOUNT_ID
from utils.commonUtil import getUuid
from utils.timeUtil import get_current_time, howLongAgo, getStrTime


ROBOT_STATE_ONLINE = 1
ROBOT_STATE_OFFLINE = 0

robot_state_cn = {
	ROBOT_STATE_OFFLINE: "离线",
	ROBOT_STATE_ONLINE: "在线"
}


def robotState_d2s(state):
	return robot_state_cn.get(state) or ""


def getRobotCount(db, cond=""):
	return db.rowcount(TB_ROBOT, cond=cond)


def getRobot_byCond(db, robotId=None, robotName=None):

	if (not robotId and not robotName):
		return None

	if (robotId):
		cond = "WHERE ID='%s'" % (robotId)
	else:
		cond = "WHERE R_Name='%s'" % (robotName)

	dbObj = db.fetchone(TB_ROBOT, cond=cond)
	if (not dbObj):
		WARNING("robot %s not exist" % cond)
		return None

	robot = WCRobot(db, dbObj=dbObj)
	robot.loadFromObj()

	return robot

def getRobot_byName(db, name):
	return getRobot_byCond(db, robotName=name)


def getRobot(db, id):
	return getRobot_byCond(db, robotId=id)


class WCRobot:

	def __init__(self, db=None, uid=None, name=None, dbObj=None):

		self.db = db
		self.myId = uid
		self.name = name
		self.uName = ""
		self.uId = ""
		self.accountId = DEFAULT_ACCOUNT_ID

		self.dbObj = dbObj

		self.role = 0
		self.state = ROBOT_STATE_OFFLINE
		self.stateCN = robotState_d2s(self.state)

		self.lastLogin = 0
		self.lastSync = 0
		self.createTime = 0

	def init(self):

		if (self.myId != 0):
			cond = "WHERE ID='%s' " % (self.myId)
		else:
			cond = "WHERE R_Name='%s' " % (self.name)

		dbObj = self.db.fetchone(TB_ROBOT, cond)
		if (not dbObj):
			return -1

		self.dbObj = dbObj

		self.loadFromObj()

		return 0

	def loadFromObj(self):

		self.myId = self.dbObj["ID"]
		self.name = self.dbObj["R_Name"]
		self.state = self.dbObj["R_State"]
		self.uId = self.dbObj["R_UId"]
		self.uName = self.dbObj["R_UName"]
		self.stateCN = robotState_d2s(self.state)
		self.lastLogin = self.dbObj["R_LastLogin"]
		self.lastSync = self.dbObj["R_LastSync"]
		self.createTime = self.dbObj["R_CreateTime"]

		return 0

	def updateLogin(self):

		robotObj = {
			"R_LastLogin": get_current_time(),
			"R_UId": self.uId,
		}

		cond = "WHERE ID='%s'" % self.myId
		ret = self.db.update(TB_ROBOT, robotObj, cond=cond)
		if (ret == -1):
			WARNING("update robot %s error for db operation" % self.name)
			return DB_ERR

	def update(self):

		robotObj = {
			"R_Name": self.name,
			"R_LastSync": get_current_time(),
		}

		cond = "WHERE ID='%s'" % self.myId
		ret = self.db.update(TB_ROBOT, robotObj, cond=cond)
		if (ret == -1):
			WARNING("update robot %s error for db operation" % self.name)
			return DB_ERR

		return 0

	def login(self):
		pass

	def add(self):

		robotObj = {
			"ID": getUuid(),
			"R_UId": self.uId,
			"R_AccountId": self.accountId,
			"R_Name": self.name,
			"R_CreateTime": get_current_time(),
			"R_LastSync": get_current_time(),
		}

		ret = self.db.insert(TB_ROBOT, robotObj)
		if (ret == -1):
			WARNING("add robot %s error for db operation" % self.name)
			return DB_ERR

		DEBUG(robotObj)

		return OCT_SUCCESS

	def delete(self):

		if (self.myId != 0):
			cond = "WHERE ID='%s'" % (self.myId)
		elif (self.name):
			cond = "WHERE R_Name='%s'" % (self.name)
		else:
			ERROR("delete robot error, both of id and robotname not specified")
			return NOT_ENOUGH_PARAS

		self.db.delete(TB_ROBOT, cond=cond)

		return 0

	def toObj(self):
		obj = {
			"id": self.myId,
			"name": self.name,
			"state": self.state,
			"stateCN": self.stateCN,
			"uId": self.uId,
			"uName": self.uName,
			"lastLogin": howLongAgo(self.lastLogin),
			"lastSync": getStrTime(self.lastSync),
			"createTime": getStrTime(self.createTime),
		}

		return obj

	def toObjBrief(self):
		
		return {
			"id": self.myId,
			"name": self.name,
		}
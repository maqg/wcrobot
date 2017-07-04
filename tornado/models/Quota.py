#!/usr/bin/python3
# -*- coding: utf-8 -*-

from conf.dbconfig import TB_QUOTA
from core.err_code import DB_ERR, OCT_SUCCESS
from core.log import DEBUG, ERROR, WARNING
from utils.commonUtil import getUuid
from utils.timeUtil import get_current_time, getStrTime


def getQuota(db, myId):

	cond = "WHERE ID='%s'" % (myId)

	dbObj = db.fetchone(TB_QUOTA, cond=cond)
	if (not dbObj):
		WARNING("quota %s not exist" % cond)
		return None

	item = Quota(db, dbObj=dbObj)
	item.loadFromObj()

	return item


QUOTA_MESSAGE_DEFAULT = 512
QUOTA_GROUP_DEFAULT = 10
QUOTA_ROBOT_DEFAULT = 5


class Quota:


	def __init__(self, db=None, myId=None, dbObj=None):

		self.db = db
		self.myId = myId
		self.dbObj = dbObj

		self.accountId = ""
		self.robots = QUOTA_ROBOT_DEFAULT
		self.messageCapacity = QUOTA_MESSAGE_DEFAULT # In MB
		self.group = QUOTA_MESSAGE_DEFAULT

		self.lastSync = 0
		self.createTime = 0

	def init(self):

		cond = "WHERE ID='%s' " % (self.myId)
		dbObj = self.db.fetchone(TB_QUOTA, cond)
		if (not dbObj):
			ERROR("init quota of %s error" % self.myId)
			return -1

		self.dbObj = dbObj
		self.loadFromObj()
		return 0

	def loadFromObj(self):

		self.myId = self.dbObj["ID"]
		self.robots = self.dbObj["Q_Robot"]
		self.messageCapacity = self.dbObj["Q_Message"]
		self.group = self.dbObj["Q_Group"]
		self.lastSync = self.dbObj["Q_LastSync"]
		self.createTime = self.dbObj["Q_CreateTime"]

	def update(self):

		userObj = {
			"Q_Robots": self.robots,
			"Q_Message": self.messageCapacity,
			"Q_Group": self.group,
			"Q_LastSync": get_current_time(),
		}

		cond = "WHERE ID='%s'" % self.myId
		ret = self.db.update(TB_QUOTA, userObj, cond=cond)
		if (ret == -1):
			WARNING("update user %s error for db operation" % self.myId)
			return DB_ERR

		return 0

	def add(self):

		userObj = {
			"ID": getUuid(),
			"Q_Robots": self.robots,
			"Q_Message": self.messageCapacity,
			"Q_Group": self.group,
			"Q_LastSync": get_current_time(),
			"Q_CreateTime": get_current_time()
		}

		ret = self.db.insert(TB_QUOTA, userObj)
		if (ret == -1):
			WARNING("add user %s error for db operation" % self.myId)
			return DB_ERR

		DEBUG(userObj)

		return OCT_SUCCESS

	def toObj(self):
		obj = {
			"id": self.myId,
			"group": self.group,
			"message": self.messageCapacity,
			"robot": self.robots,
			"lastSync": getStrTime(self.lastSync),
			"createTime": getStrTime(self.createTime),
		}

		return obj

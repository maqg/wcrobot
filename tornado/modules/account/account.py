#!usr/bin/python
# -*- coding: utf-8 -*- 

import time
from binascii import crc32 as CRC32

from core import dbmysql
from core.err_code import USER_ALREADY_EXIST, UNACCP_PARAS
from models.Account import *
from models.Common import DEFAULT_ACCOUNT

AUTHKEY_TIMEOUT = 24 * 30 * 60


def get_userlist(db):
	user_list = []

	ret = db.select(TB_ACCOUNT, cond="")
	if ret == -1:
		ERROR("get user list error")
		return (DB_ERR, None)

	for dur in db.cur:
		obj = dbmysql.row_to_dict(TB_ACCOUNT, dur)
		temp = {
			"id": obj["ID"],
			"name": obj["U_Name"],
		}
		user_list.append(temp)

	DEBUG(user_list)

	return (OCT_SUCCESS, user_list)


def get_alluser(db, arg):
	listObj = {
		"total": 0,
		"users": [],
	}

	start = arg["paras"].get("start") or 0
	limit = arg["paras"].get("limit") or 100

	cond = "WHERE 1=1 "
	ret = db.select(TB_ACCOUNT, cond=cond, limit=int(limit), offset=int(start))
	if ret == -1:
		ERROR("get user list error")
		return (DB_ERR, None)

	for dur in db.cur:
		obj = dbmysql.row_to_dict(TB_ACCOUNT, dur)
		user = Account(db, dbObj=obj)
		user.loadFromObj()
		user.loadQuota()

		listObj["users"].append(user.toObj())

	listObj["total"] = getUserCount(db)

	return (OCT_SUCCESS, listObj)


def get_user(db, userId):
	user = Account(db, userId)

	if (user.init() != 0):
		ERROR("user %s not exist" % userId)
		return (USER_NOT_EXIST, None)

	return (OCT_SUCCESS, user.toObj())


def add_user(db, arg):

	user = getUser(db, userName=arg["paras"].get("account"))
	if (user):
		WARNING("user %s already exist" % arg["paras"].get("account"))
		return USER_ALREADY_EXIST

	user = Account(db)

	user.name = arg["paras"].get("account")
	user.password = arg["paras"].get("password")

	if (not user.name or not user.password):
		ERROR("not username or password specified")
		return NOT_ENOUGH_PARAS

	user.ukey = arg["paras"].get("ukey")
	user.email = arg["paras"].get("email") or ""
	user.phone = arg["paras"].get("phoneNumber") or ""

	return user.add()


def delete_user(db, userId):
	user = getUser(db, userId=userId)
	if (not user):
		ERROR("account %s not exist" % (userId))
		return USER_NOT_EXIST

	if (user.name == DEFAULT_ACCOUNT):
		ERROR("account %s is super admin, forbid delete." % (userId))
		return UNACCP_PARAS

	return user.delete()


def reset_password(db, arg):
	user = getUser(db, userId=arg["paras"].get("id"))
	if (not user):
		ERROR("user %s not exist" % (arg["paras"].get("id")))
		return USER_NOT_EXIST

	return user.resetPassword(arg["paras"].get("password"))


def update_user(db, arg):
	user = getUser(db, userId=arg["paras"].get("id"))
	if (not user):
		ERROR("user %s not exist" % (arg["paras"].get("id")))
		return USER_NOT_EXIST

	user.email = arg["paras"].get("email") or ""
	user.phone = arg["paras"].get("phoneNumber") or ""
	user.ukey = arg["paras"].get("ukey") or ""

	return user.update()

def change_password(db, arg):
	user = getUser(db, userId=arg["paras"].get("id"))
	if (not user):
		ERROR("user %s not exist" % (arg["paras"].get("id")))
		return USER_NOT_EXIST

	return user.changePassword(arg["paras"].get('oldPassword'),
	                           arg["paras"].get('newPassword'))


def getUserByName(db, name):
	return getUser(db, userName=name)


def check_timestamp(incomingTime):
	currentTime = int(time.time())
	if (abs(currentTime - int(incomingTime)) > AUTHKEY_TIMEOUT):  # 30 minutes
		ERROR("Timestamp check error [%s]" % (incomingTime))
		return False

	return True


def check_CRC(rand, user, client, timestamp, crc):
	CRCStr = rand + user + client + timestamp
	CRCStr += "OCTopus Link OAuth"
	CRCValue = CRC32(CRCStr) & 0xffffffff
	if (CRCValue != int(crc)):
		ERROR("CRC check error [%s]" % (CRCStr))
		return False

	return True


def check_Client_CRC(rand, timestamp, crc):
	CRCStr = rand + timestamp
	CRCStr += "OCTopus Link OAuth"
	CRCValue = CRC32(CRCStr) & 0xffffffff
	if (CRCValue != int(crc)):
		ERROR("CRC check error [%s]" % (CRCStr))
		return False

	return True

#!usr/bin/python
# -*- coding: utf-8 -*- 

from core.err_code import OCT_SUCCESS, USER_PASSWD_ERR, DB_ERR, USER_NOT_EXIST
from modules.account import account as userService
from utils.commonUtil import buildRetObj, b64_decode
from utils.sessionUtil import newSession, removeSession


def web_get_user(db, env, arg):
    userId = arg["paras"].get("id")
    if userId == None:
        ret, data = userService.get_alluser(db, arg)
    else:
        ret, data = userService.get_user(db, userId)

    return buildRetObj(ret, data)


def web_get_userlist(db, env, arg):
    (ret, data) = userService.get_userlist(db)
    return buildRetObj(ret, data)


def web_add_user(db, env, arg):
    ret = userService.add_user(db, arg)
    return buildRetObj(ret)


def web_del_user(db, env, arg):
    ret = userService.delete_user(db, arg["paras"]["id"])
    return buildRetObj(ret)


def web_login(db, env, arg):
    paras = arg["paras"]
    user = userService.getUserByName(db, paras.get("account"))
    if (not user):
        return buildRetObj(USER_NOT_EXIST, None)

    ret = user.auth(b64_decode(paras.get("password")))
    if ret == 0:
        data = {
            "id": user.myId,
            "name": user.name,
            "role": user.role
        }
        sessionObj = newSession(db, data)
        data["session"] = sessionObj
        return buildRetObj(OCT_SUCCESS, data)
    else:
        return buildRetObj(USER_PASSWD_ERR)


def web_ukeylogin(db, env, arg):
    user = userService.getUserByUkey(db, str(arg["paras"].get("ukey")))
    if (not user):
        return buildRetObj(USER_NOT_EXIST, None)

    ret = user.authUkey(arg["paras"].get("ukey"))
    if ret == 0:
        data = {
            'id': user.uid,
            'ukey': user.ukey,
            'name': user.name,
            'role': user.role
        }
        return buildRetObj(OCT_SUCCESS, data)

    elif ret == -2:
        return buildRetObj(USER_PASSWD_ERR)

    else:
        return buildRetObj(DB_ERR)


def web_logout(db, env, arg):

    paras = arg["paras"]
    sessionId = paras.get("sessionUuid")
    removeSession(db, sessionId)

    return buildRetObj(OCT_SUCCESS)


def web_modify_password(db, env, arg):
    ret = userService.change_password(db, arg)
    return buildRetObj(ret)


def web_reset_password(db, env, arg):
    ret = userService.reset_password(db, arg)
    return buildRetObj(ret)


def web_update_user(db, env, arg):
    ret = userService.update_user(db, arg)
    return buildRetObj(ret)

def web_update_quota(db, env, arg):
    ret = userService.update_quota(db, arg)
    return buildRetObj(ret)
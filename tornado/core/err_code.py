#!/usr/bin/python
# -*- coding: utf-8 -*-

OCT_SUCCESS = 0
NOT_ENOUGH_PARAS = 1
TOO_MANY_PARAS = 2
UNACCP_PARAS = 3
XML_ERR = 4
EXEC_CMD_ERR = 5
COMMON_ERR = 6
SEGMENT_NOT_EXIST = 7
SEGMENT_ALREADY_EXIST = 8
FILE_NOT_EXIST = 9
ADDED_TO_TASK = 10
ADDED_TO_SERVER = 11
TIME_OUT = 12
CHECK_ENV_ERR = 13
SEND_MSG_FAILED = 14
INCOMPATIBLE_CONFIG = 17
DROPPED_INTERFACE = 18
UNMATCHED_TEMPLATE_FORMAT = 19
PERMISSION_NOT_ENOUGH = 20
CONFIG_NOT_EXIST = 256
LAZY_PROGRAMMER = 257
NO_CMD = 258
OPE_FORBID = 259
INVALID_CONFIG_FILE = 260
CONFIG_ALREADY_EXIST = 261
SYSCALL_ERR = 262
OCT_SYSTEM_ERR = 263
NO_AUTH_SKEY = 264
WRONG_AUTH_SKEY = 265
WRONG_AUTH_TIMESTAMP = 266
BAD_NSIS_ENV = 267
MAKE_NSIS_ERR = 268
USER_INVALID_NAME = 518
DB_ERR = 519
USER_PASSWD_ERR = 520
USER_NOT_EXIST = 521
USER_ALREADY_EXIST = 522

err_desc_ch = {
	OCT_SUCCESS: "执行成功",
	NOT_ENOUGH_PARAS: "参数不够",
	TOO_MANY_PARAS: "参数太多",
	UNACCP_PARAS: "参数错误",
	XML_ERR: "XML解析错误",
	EXEC_CMD_ERR: "命令执行错误",
	COMMON_ERR: "通用错误",
	SEGMENT_NOT_EXIST: "字段不存在",
	SEGMENT_ALREADY_EXIST: "字段已经存在",
	FILE_NOT_EXIST: "文件不存在",
	ADDED_TO_TASK: "已添加到任务队列中",
	ADDED_TO_SERVER: "服务器端运行中",
	TIME_OUT: "等待超时",
	CHECK_ENV_ERR: "环境检测失败",
	SEND_MSG_FAILED: "发送消息失败",
	INCOMPATIBLE_CONFIG: "不兼容的配置",
	DROPPED_INTERFACE: "该接口已废弃",
	UNMATCHED_TEMPLATE_FORMAT: "模板格式不匹配",
	PERMISSION_NOT_ENOUGH: "权限不足",
	CONFIG_NOT_EXIST: "配置文件不存在",
	LAZY_PROGRAMMER: "此功能未实现",
	NO_CMD: "没有此命令",
	OPE_FORBID: "禁止此操作",
	INVALID_CONFIG_FILE: "配置文件不合法",
	CONFIG_ALREADY_EXIST: "配置文件已经存在",
	SYSCALL_ERR: "系统调用错误",
	OCT_SYSTEM_ERR: "系统错误",
	NO_AUTH_SKEY: "没有URL认证密码",
	WRONG_AUTH_SKEY: "错误的URL认证密码",
	WRONG_AUTH_TIMESTAMP: "错误的URL认证时间戳，请同步你的客户机时间",
	BAD_NSIS_ENV: "没有安装JRE或者NSIS工具包",
	MAKE_NSIS_ERR: "制作NSIS安装包失败",
	USER_INVALID_NAME: "用户错误",
	DB_ERR: "数据库错误",
	USER_PASSWD_ERR: "用户名密码不匹配",
	USER_NOT_EXIST: "用户不存在",
	USER_ALREADY_EXIST: "用户已存在"
}

err_desc_en = {
	OCT_SUCCESS: "Command success",
	NOT_ENOUGH_PARAS: "Not enough parameters",
	TOO_MANY_PARAS: "Too many parameters",
	UNACCP_PARAS: "Invalid parameters",
	XML_ERR: "XML Error",
	EXEC_CMD_ERR: "Execute Command Error",
	COMMON_ERR: "Common error",
	SEGMENT_NOT_EXIST: "Segment not exist",
	SEGMENT_ALREADY_EXIST: "Segment already exist",
	FILE_NOT_EXIST: "File not exist",
	ADDED_TO_TASK: "Added to task",
	ADDED_TO_SERVER: "Added to server",
	TIME_OUT: "Time out",
	CHECK_ENV_ERR: "check env err",
	SEND_MSG_FAILED: "send msg failed",
	INCOMPATIBLE_CONFIG: "incompatible config",
	DROPPED_INTERFACE: "dropped interface",
	UNMATCHED_TEMPLATE_FORMAT: "unmatched template_format",
	PERMISSION_NOT_ENOUGH: "Permissions Not Enough",
	CONFIG_NOT_EXIST: "Config file not exist",
	LAZY_PROGRAMMER: "Not Complete This Function",
	NO_CMD: "No This Commond",
	OPE_FORBID: "Forbid this peration",
	INVALID_CONFIG_FILE: "Invalid config file",
	CONFIG_ALREADY_EXIST: "Config file already exists",
	SYSCALL_ERR: "System call error",
	OCT_SYSTEM_ERR: "System error",
	NO_AUTH_SKEY: "No skey specified",
	WRONG_AUTH_SKEY: "Wrong auth skey",
	WRONG_AUTH_TIMESTAMP: "Wrong auth timestamp,please sync your system time",
	BAD_NSIS_ENV: "no jre or makensis installed",
	MAKE_NSIS_ERR: "make nsis package error",
	USER_INVALID_NAME: "Invalid user name",
	DB_ERR: "Database Error",
	USER_PASSWD_ERR: "User and Password not match",
	USER_NOT_EXIST: "User Not Exist",
	USER_ALREADY_EXIST: "User Already Exist",
}

def print_retmsg(buff):
	print('\n%% %s\n' % buff)
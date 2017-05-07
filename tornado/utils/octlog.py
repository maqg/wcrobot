#!usr/bin/python
# -*- coding: utf-8 -*-

import sys

from utils.commonUtil import isSystemWindows

sys.path.append("../")

import settings
import ctypes

EV_LEVEL_EMERG = 0
EV_LEVEL_ALERT = 1
EV_LEVEL_CRIT = 2
EV_LEVEL_ERROR = 3
EV_LEVEL_WARN = 4
EV_LEVEL_NOTIFY = 5
EV_LEVEL_INFO = 6
EV_LEVEL_DEBUG = 7

event_level = {
	EV_LEVEL_EMERG: "Emerg",
	EV_LEVEL_ALERT: "Alert",
	EV_LEVEL_CRIT: "Crit",
	EV_LEVEL_ERROR: "Error",
	EV_LEVEL_WARN: "Warn",
	EV_LEVEL_NOTIFY: "Notify",
	EV_LEVEL_INFO: "Info",
	EV_LEVEL_DEBUG: "Debug"
}

if (isSystemWindows()):
	pylog = None
else:
	pylog = ctypes.CDLL(settings.PRODUCT_HOME + '/lib/libpylog_lib.so')

BAD_MMAP_RESULT = "BadResult"

def get_api_record():
	ret = pylog.get_api_record()
	if (ret == -1):
		return False

	return ret and True or False

def get_debug_level(mod):
	if (mod == None or mod < 0):
		return EV_LEVEL_NOTIFY

	func = pylog.get_debug_level
	func.restype = ctypes.c_char_p
	ret = func(int(mod))
	if (ret == BAD_MMAP_RESULT):
		return EV_LEVEL_NOTIFY

	return int(ret)

def get_log_level(mod):
	if (mod == None or mod < 0):
		return EV_LEVEL_NOTIFY

	func = pylog.get_log_level
	func.restype = ctypes.c_char_p
	ret = func(int(mod))
	if (ret == BAD_MMAP_RESULT):
		return EV_LEVEL_NOTIFY

	return int(ret)

def set_log_level(mod=-1, levels=str(EV_LEVEL_ERROR)):
	return pylog.set_log_level(int(mod or -1), levels)

def set_debug_level(mod=-1, levels=str(EV_LEVEL_ERROR)):
	return pylog.set_debug_level(int(mod or -1), levels)

def set_api_record(state):
	return pylog.set_api_record(int(state))

if __name__ == "__main__":
	print(get_log_level(1))
	print(get_log_level(2))
	print(get_debug_level(2))

	print(set_debug_level(6, "7"))
	print(get_log_level(6))
	print(set_api_record(1))
	print(get_api_record())

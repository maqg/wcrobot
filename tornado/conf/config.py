#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time

from core.modules_code import MOD_WEBUI, MOD_OTHER
from utils.commonUtil import isSystemWindows
from utils.octlog import get_debug_level, get_log_level

API_TEST_KEY = "00000000000000000000000000000000"

PROJECT_PATH = os.path.dirname(__file__)[:-5]

LOG_FILE_PATH = PROJECT_PATH + os.sep + "var" + os.sep + "logs" + os.sep
TMP_FILE_PATH = PROJECT_PATH + os.sep + "var" + os.sep + "tmp" + os.sep

OCTFRAME_LOG_LEVEL = 7
OCTFRAME_LOG_MAX_LEN = 1024000

LVL_EMERG = 0
LVL_ALERT = 1
LVL_CRIT = 2
LVL_ERROR = 3
LVL_WARN = 4
LVL_NOTIFY = 5
LVL_INFO = 6
LVL_DEBUG = 7

LOG_LEVELS = ["Emerg", "Alert", "Crit", "Error", "Warn", "Notify", "Info", "Debug"]

MAX_USING_TIMEOUT = 10 # seconds

LOG_HOST = "127.0.0.1"
LOG_PORT = 62514

CENTER_PORT = 6443
SERVER_PORT = 5443
OCTBS_PORT = 4443
VR_PORT = 3443
CONSOLEPROXY_PORT = 2443

CONFIG_FILE = PROJECT_PATH + os.sep + "var" + os.sep + "config.json"

def getSystemConf():

	if (not SystemConf.inited):
		SystemConf()

	return SystemConf

class SystemConf():

	version = "5.0"
	inited = False
	debugLevel = -1
	system = "center"
	lastLevelUpdateTime = 0

	def init(self, debugLevel=None):
		pass

	def __init__(self, debugLevel=None):

		now = int(time.time())
		if (abs(now - SystemConf.lastLevelUpdateTime) >= MAX_USING_TIMEOUT or SystemConf.debugLevel == -1):
			if (isSystemWindows()):
				SystemConf.debugLevel = LVL_DEBUG
			else:
				SystemConf.debugLevel = get_debug_level(MOD_WEBUI)
			SystemConf.lastLevelUpdateTime = now

		if (not SystemConf.inited):
			pass
#			SystemConf.inited = True

	@staticmethod
	def toObj():

		return {
			"version": SystemConf.version,
			"system": SystemConf.system,
			"debugLevel": SystemConf.debugLevel,
			"lastLevelUpdateTime": SystemConf.lastLevelUpdateTime
		}

def getSystemLogConf():

	if (not SystemLogConf.inited):
		SystemLogConf()

	return SystemLogConf

class SystemLogConf():

	version = "5.0"
	inited = False
	logLevels = {}
	logLevel = -1
	lastLevelUpdateTime = 0

	def init(self, logLevel=None):
		pass

	def __init__(self, logLevel=None):

		now = int(time.time())
		if (abs(now - SystemLogConf.lastLevelUpdateTime) >= MAX_USING_TIMEOUT or SystemLogConf.logLevels == {}):
			for mod in range(0, MOD_OTHER + 1):
				if (isSystemWindows()):
					level = LVL_DEBUG
				else:
					level = get_log_level(MOD_WEBUI)
				SystemLogConf.logLevels[mod] = level

			SystemLogConf.lastLevelUpdateTime = now

		if (not SystemLogConf.inited):
			pass

	@staticmethod
	def toObj():

		return {
			"version": SystemLogConf.version,
			"debugLevel": SystemLogConf.logLevel,
			"lastLevelUpdateTime": SystemLogConf.lastLevelUpdateTime
		}

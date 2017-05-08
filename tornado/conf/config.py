#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time

from core.modules_code import MOD_WEBUI, MOD_OTHER
from utils.commonUtil import isSystemWindows, fileToObj

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

MAX_USING_TIMEOUT = 10  # seconds

LOG_HOST = "127.0.0.1"
LOG_PORT = 62514

CENTER_PORT = 6443
SERVER_PORT = 5443
OCTBS_PORT = 4443
VR_PORT = 3443
CONSOLEPROXY_PORT = 2443

CONFIG_FILE = PROJECT_PATH + os.sep + "config.json"


def getSystemConf():

	if (not SystemConf.inited):
		SystemConf()

	return SystemConf


class SystemConf():

	version = "0.1"
	inited = False
	debugLevel = LVL_WARN
	system = "wcrobot"

	def __init__(self, debugLevel=None):

		config = fileToObj(CONFIG_FILE)
		if config:
			SystemConf.debugLevel = config["debug"]

	@staticmethod
	def toObj():

		return {
			"version": SystemConf.version,
			"system": SystemConf.system,
			"debugLevel": SystemConf.debugLevel
		}

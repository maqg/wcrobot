#!usr/bin/python
# -*- coding: utf-8 -*-
from conf.config import SystemConf
from models.Robot import *

AUTHKEY_TIMEOUT = 24 * 30 * 60


def show_config(db, arg):
	config = SystemConf.toObj()
	return (OCT_SUCCESS, config)

def show_systeminfo(db, arg):
	info = {
		"accounts": 10,
		"robots": 100,
		"messages": 10000,
	}

	return (OCT_SUCCESS, info)


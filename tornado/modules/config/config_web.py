#!usr/bin/python
# -*- coding: utf-8 -*-

from modules.config.config import show_config, show_systeminfo
from utils.commonUtil import buildRetObj


def web_show_config(db, env, arg):
	ret, data = show_config(db, arg)
	return buildRetObj(ret, data)


def web_show_systeminfo(db, env, arg):
	ret, data = show_systeminfo(db, arg)
	return buildRetObj(ret, data)

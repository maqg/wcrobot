#!/usr/bin/python
# -*- coding: utf-8 -*-

from models.Account import ROLE_SUPERADMIN, ROLE_ADMIN

moduleName = "config"

funcList = {

	"APIShowConfig": {
		"name": "查看系统配置",
		"serviceName": "config.config_web.web_show_config",
		"roles": [ROLE_SUPERADMIN, ROLE_ADMIN],
		"paras": {	}
	},

	"APIShowSystemInfo": {
		"name": "查看系统信息",
		"serviceName": "config.config_web.web_show_systeminfo",
		"roles": [ROLE_SUPERADMIN, ROLE_ADMIN],
		"paras": {}
	}


}
#!/usr/bin/python
# -*- coding: utf-8 -*-

from models.Account import ROLE_SUPERADMIN, ROLE_ADMIN
from views.api.center.api import *

moduleName = "robot"

funcList = {

	"APIAddRobot": {
		"name": "添加机器人",
		"serviceName": "robot.robot_web.web_add_robot",
		"roles": [ROLE_SUPERADMIN, ROLE_ADMIN],
		"paras": {
			"name": {
				"type": PARAM_TYPE_STRING,
				"descCN": "机器人名称",
				"default": "NotNull"
			},
			"uid": {
				"type": PARAM_TYPE_STRING,
				"descCN": "微信ID",
				"default": ""
			},
			"phoneNumber": {
				"type": PARAM_TYPE_STRING,
				"descCN": "电话号码",
				"default": ""
			}
		}
	},

	"APILogin": {
		"name": "生成登录二维码",
		"serviceName": "robot.robot_web.web_login",
		"paras": {
			"id": {
				"type": PARAM_TYPE_STRING,
				"descCN": "机器人Id",
				"default": "NotNull"
			}
		}
	},

	"APIShowRobot": {
		"name": "获取单个机器人信息",
		"serviceName": "robot.robot_web.web_get_robot",
		"roles": [ROLE_SUPERADMIN, ROLE_ADMIN],
		"paras": {
			"id": {
				"type": PARAM_TYPE_STRING,
				"descCN": "机器人Id",
				"default": "NotNull"
			}
		}
	},

	"APIShowAllRobot": {
		"name": "获取所有机器人",
		"serviceName": "robot.robot_web.web_get_allrobot",
		"roles": [ROLE_SUPERADMIN, ROLE_ADMIN],
		"paras": {
			"start": {
				"type": PARAM_TYPE_INT,
				"descCN": "开始位置",
				"default": 0
			},
			"limit": {
				"type": PARAM_TYPE_INT,
				"descCN": "获取条目",
				"default": 15
			},
			"sName": {
				"type": PARAM_TYPE_STRING,
				"descCN": "名称",
				"default": ""
			},
			"sUId": {
				"type": PARAM_TYPE_STRING,
				"descCN": "微信Id",
				"default": ""
			}
		}
	},

	"APIShowRobotList": {
		"name": "获取账号列表",
		"roles": [ROLE_SUPERADMIN],
		"serviceName": "robot.robot_web.web_get_robotlist",
		"paras": {
			"accountId": {
				"type": PARAM_TYPE_STRING,
				"descCN": "账号Id",
				"default": ""
			}
		}
	},

	"APIDeleteRobot": {
		"name": "删除单个机器人",
		"roles": [ROLE_SUPERADMIN, ROLE_ADMIN],
		"serviceName": "robot.robot_web.web_del_robot",
		"paras": {
			"id": {
				"type": PARAM_TYPE_STRING,
				"descCN": "机器人Id",
				"default": "NotNull"
			}
		}
	},

	"APIUpdateRobot": {
		"name": "编辑机器人信息",
		"roles": [ROLE_SUPERADMIN, ROLE_ADMIN],
		"serviceName": "robot.robot_web.web_update_robot",
		"paras": {
			"id": {
				"type": PARAM_TYPE_STRING,
				"descCN": "Robot UUID",
				"default": "NotNull"
			},
			"name": {
				"type": PARAM_TYPE_STRING,
				"descCN": "机器人名称",
				"default": ""
			},
			"phoneNumber": {
				"type": PARAM_TYPE_STRING,
				"descCN": "电话号码",
				"default": ""
			}
		}
	},

	"APILogOut": {
		"name": "退出登录",
		"roles": [ROLE_SUPERADMIN, ROLE_ADMIN],
		"serviceName": "robot.robot_web.web_logout",
		"paras": {
			"id": {
				"type": PARAM_TYPE_STRING,
				"desc": "UUID of Robot",
				"descCN": "Robot Id",
				"default": "NotNull"
			}
		}
	}
}

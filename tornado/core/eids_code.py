#!/usr/bin/python
# -*- coding: utf-8 -*-

from core.modules_code import *

EID_DC_ADD = 393216
EID_DC_DELETE = 393217
EID_DC_UPDATE = 393218
EID_DC_DISPLAY = 393219
EID_USER_LOGIN = 393226
EID_USER_ADD = 393227
EID_USER_DELETE = 393229
EID_USER_UPDATE = 393230
EID_USER_PASSWORD = 393231
EID_USER_LOGOUT = 393232
EID_USER_DSIPLAY = 393233
EID_USER_SSOVM = 393234
EID_USER_UKEYLOGIN = 393235
EID_HOSTPOOL_ADD = 393236
EID_HOSTPOOL_DELETE = 393237
EID_HOSTPOOL_UPDATE = 393238
EID_HOSTPOOL_DISPLAY = 393239
EID_HOST_TAKEOVER = 393246
EID_HOST_RELEASE = 393247
EID_HOST_UPDATE = 393248
EID_HOST_DISPLAY = 393249
EID_HOST_SHUTDOWN = 393250
EID_HOST_RESTART = 393251
EID_HOST_ONLINE = 393252
EID_HOST_OFFLINE = 393253
EID_HOST_UPGRADE = 393254
EID_HOST_PATCH = 393255
EID_HOST_SYNCTIME = 393256
EID_VM_CREATE = 393266
EID_VM_POWER = 393267
EID_VM_BATCH_POWER = 393268
EID_VM_DELETE = 393269
EID_VM_BATCH_DELETE = 393270
EID_VM_SNAP_ADD = 393271
EID_VM_SNAP_DELETE = 393272
EID_VM_SNAP_MERGE = 393273
EID_VM_SNAP_UPDATE = 393274
EID_VM_DISPLAY = 393275
EID_VM_SET_CPU = 393276
EID_VM_SET_MEMORY = 393277
EID_VM_CREATE_TEMPLATE = 393278
EID_VM_UPDATE = 393279
EID_VM_DISK_ADD = 393280
EID_VM_DISK_DELETE = 393281
EID_VM_CDROM_ADD = 393282
EID_VM_CDROM_DELETE = 393283
EID_VM_IF_SET = 393284
EID_VM_IF_BIND = 393285
EID_VM_IF_RATE = 393286
EID_VM_IF_VLAN_SET = 393287
EID_VM_IF_CREATE = 393288
EID_VM_IF_DELETE = 393289
EID_VM_ISO_ADD = 393290
EID_VM_ISO_DELETE = 393291
EID_VM_MIGRATE = 393292
EID_VM_CHANGE_OS = 393293
EID_IPPOOL_DISPLAY = 393316
EID_IPPOOL_ADD = 393317
EID_IPPOOL_UPDATE = 393318
EID_IPPOOL_DELETE = 393319
EID_VG_DISPLAY = 393326
EID_VG_ADD = 393327
EID_VG_UPDATE = 393328
EID_VG_DELETE = 393329
EID_VG_ALLOWVM = 393330
EID_VG_DISALLOWVM = 393331
EID_VG_BATCH_OPERATE = 393332
EID_VG_BATCH_CREATE = 393333
EID_LOG_DISPLAY = 393336
EID_LOG_SET = 393337
EID_STORAGE_DISPLAY = 393346
EID_STORAGE_ADD = 393347
EID_STORAGE_DELETE = 393348
EID_TEMPLATE_DISPLAY = 393356
EID_TEMPLATE_ADD = 393357
EID_TEMPLATE_DELETE = 393358
EID_TASK_CREATE = 150
EID_TASK_START = 151
EID_TASK_FINISH = 152
EID_TASK_RUNNING_IN_SERVER = 153
EID_DASHBOARD_CPU = 393376
EID_DASHBOARD_RRDCPU = 393377
EID_DASHBOARD_MEMORY = 393378
EID_DASHBOARD_RRDMEMORY = 393379
EID_DASHBOARD_MEMORYVM = 393380
EID_DASHBOARD_LICENSE = 393381
EID_DASHBOARD_HOSTVM = 393382
EID_DASHBOARD_STORAGE = 393383
EID_DASHBOARD_STORAGEVM = 393384
EID_DNS_DISPLAY = 393386
EID_DNS_SET = 393387
EID_HA_DISPLAY = 393397
EID_HA_SET_STATE = 393398
EID_HA_SET_CONFIG = 393399
EID_HA_PROPOSE_MASTER = 393400
EID_HA_EXCLUDE = 393401
EID_NETWORK_INTERFACE_GET_LIST = 393407
EID_NETWORK_INTERFACE_GET_INFO = 393408
EID_NETWORK_INTERFACE_SET_CONFIG = 393409
EID_NETWORK_INTERFACE_DEL = 393410
EID_NETWORK_ROUTE_GET_LIST = 393411
EID_NETWORK_ROUTE_SET = 393412
EID_NETWORK_ROUTE_DEL = 393413
EID_SYSTEM_LICENSE_UPLOAD = 393417
EID_LOGS_SET_LOG_LEVEL = 393467
EID_LOGS_SET_DEBUG_LEVEL = 393468
EID_LOGS_SET_APIRECORD_STATE = 393469
EID_LOGS_SET_REMOTE_LOG = 393470
EID_PATCH_DISPLAY = 393477
EID_PATCH_ADD = 393478
EID_PATCH_DEL = 393479
EID_PATCH_SET_STATE = 393480
EID_PATCH_SYSTEM_DISPLAY = 393481
EID_PATCH_SYSTEM_ADD = 393482
EID_PATCH_SERVER_DISPLAY = 393483
EID_PATCH_SERVER_ADD = 393484
EID_PATCH_SERVER_DEL = 393485
EID_PATCH_SERVER_UPGRADE = 393486
EID_ALARM_TYPE_DISPLAY = 393497
EID_ALARM_METHOD_DISPLAY = 393498
EID_ALARM_METHOD_ADD = 393499
EID_ALARM_METHOD_UPDATE = 393500
EID_ALARM_METHOD_DELETE = 393501
EID_ALARM_RULE_DISPLAY = 393502
EID_ALARM_RULE_ADD = 393503
EID_ALARM_RULE_UPDATE = 393504
EID_ALARM_RULE_DELETE = 393505
EID_PROCESS_STATUS_CHANGES = 393506
EID_CLIENTPOLICY_ADD = 393516
EID_CLIENTPOLICY_DELETE = 393517
EID_CLIENTPOLICY_UPDATE = 393518
EID_CLIENTPOLICY_DSIPLAY = 393519
EID_USERGROUP_ADD = 393526
EID_USERGROUP_DELETE = 393527
EID_USERGROUP_UPDATE = 393528
EID_USERGROUP_DSIPLAY = 393529
EID_USERGROUP_BINDUSER = 393530
EID_USERGROUP_BINDCLIENTPOLICY = 393531
EID_VMOFFERING_ADD = 393532
EID_VMOFFERING_DELETE = 393533
EID_VMOFFERING_UPDATE = 393534
EID_VMOFFERING_DISPLAY = 393535
EID_DISKOFFERING_ADD = 393536
EID_DISKOFFERING_DELETE = 393537
EID_DISKOFFERING_UPDATE = 393538
EID_DISKOFFERING_DISPLAY = 393539
EID_VROFFERING_ADD = 393540
EID_VROFFERING_DELETE = 393541
EID_VROFFERING_UPDATE = 393542
EID_VROFFERING_DISPLAY = 393543

eids_en = {
	EID_DC_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add DC [%s]",
		"formatCN": "添加数据中心[%s]",
	},
	EID_DC_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "Delelte DC [%s]",
		"formatCN": "删除数据中心[%s]",
	},
	EID_DC_UPDATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Update DC [%s]",
		"formatCN": "更新数据中心[%s]",
	},
	EID_DC_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Display DC [%s]",
		"formatCN": "查看数据中心[%s]",
	},
	EID_USER_LOGIN: {
		"mid": MOD_WEBUI,
		"formatEN": "User [%s] login",
		"formatCN": "用户[%s]登录",
	},
	EID_USER_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add [%s]",
		"formatCN": "添加用户[%s]",
	},
	EID_USER_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "User [%s] delete",
		"formatCN": "删除用户[%s]",
	},
	EID_USER_UPDATE: {
		"mid": MOD_WEBUI,
		"formatEN": "User [%s] update",
		"formatCN": "用户[%s]成功更新",
	},
	EID_USER_PASSWORD: {
		"mid": MOD_WEBUI,
		"formatEN": "User [%s] update password",
		"formatCN": "用户[%s]修改密码",
	},
	EID_USER_LOGOUT: {
		"mid": MOD_WEBUI,
		"formatEN": "User [%s] logout",
		"formatCN": "用户[%s]登出",
	},
	EID_USER_DSIPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Display user [%s]",
		"formatCN": "查询用[%s]",
	},
	EID_USER_SSOVM: {
		"mid": MOD_WEBUI,
		"formatEN": "Set ssovm [%s]",
		"formatCN": "设置ssovm[%s]",
	},
	EID_USER_UKEYLOGIN: {
		"mid": MOD_WEBUI,
		"formatEN": "User [%s] ukeylogin",
		"formatCN": "用户[%s]ukeylogin",
	},
	EID_HOSTPOOL_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add Host Pool [%s]",
		"formatCN": "添加主机池[%s]",
	},
	EID_HOSTPOOL_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "Delelte Host Pool [%s]",
		"formatCN": "删除主机池[%s]",
	},
	EID_HOSTPOOL_UPDATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Update Host Pool [%s]",
		"formatCN": "更新主机池[%s]",
	},
	EID_HOSTPOOL_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Display Host Pool [%s]",
		"formatCN": "查询主机池[%s]",
	},
	EID_HOST_TAKEOVER: {
		"mid": MOD_WEBUI,
		"formatEN": "Take over Host [%s]",
		"formatCN": "接管主机[%s]",
	},
	EID_HOST_RELEASE: {
		"mid": MOD_WEBUI,
		"formatEN": "Release Host [%s]",
		"formatCN": "解除接管主机[%s]",
	},
	EID_HOST_UPDATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Update Host [%s]",
		"formatCN": "更新主机[%s]",
	},
	EID_HOST_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Display Host [%s]",
		"formatCN": "查看主机[%s]",
	},
	EID_HOST_SHUTDOWN: {
		"mid": MOD_WEBUI,
		"formatEN": "Shutdown Host [%s]",
		"formatCN": "关闭主机[%s]",
	},
	EID_HOST_RESTART: {
		"mid": MOD_WEBUI,
		"formatEN": "Restart Host [%s]",
		"formatCN": "重启主机[%s]",
	},
	EID_HOST_ONLINE: {
		"mid": MOD_WEBUI,
		"formatEN": "Online Host [%s]",
		"formatCN": "上线主机[%s]",
	},
	EID_HOST_OFFLINE: {
		"mid": MOD_WEBUI,
		"formatEN": "Offline Host [%s]",
		"formatCN": "下线主机[%s]",
	},
	EID_HOST_UPGRADE: {
		"mid": MOD_WEBUI,
		"formatEN": "Upgrade Host [%s] to version [%s]",
		"formatCN": "升级主机[%s]，新版本为[%s]",
	},
	EID_HOST_PATCH: {
		"mid": MOD_WEBUI,
		"formatEN": "To patch Host [%s] with patch [%s]",
		"formatCN": "为主机[%s]进行补丁维护，补丁包为[%s]",
	},
	EID_HOST_SYNCTIME: {
		"mid": MOD_WEBUI,
		"formatEN": "To sync time for host [%s]",
		"formatCN": "为主机[%s]进行时间校正",
	},
	EID_VM_CREATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Vm [%s] created,cpu:[%d],memory:[%d],template:[%s]",
		"formatCN": "创建虚拟机[%s]，内存：[%d]，CPU：[%d]，模板：[%s]",
	},
	EID_VM_POWER: {
		"mid": MOD_WEBUI,
		"formatEN": "Vm [%s] get power opertaion [%s]",
		"formatCN": "虚拟机[%s]执行电源操作[%s]",
	},
	EID_VM_BATCH_POWER: {
		"mid": MOD_WEBUI,
		"formatEN": "get power operation [%s] for vm list [%s]",
		"formatCN": "执行批量电源操作[%s]，虚拟机列表：[%s]",
	},
	EID_VM_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "Delete VM [%s]",
		"formatCN": "删除虚拟机[%s]",
	},
	EID_VM_BATCH_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "Delete VM [%s]",
		"formatCN": "批量删除虚拟机[%s]",
	},
	EID_VM_SNAP_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "VM [%s] add snap [%s]",
		"formatCN": "为虚拟机[%s]添加snap[%s]",
	},
	EID_VM_SNAP_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "VM [%s] delete snap [%s]",
		"formatCN": "虚拟机[%s]删除snap[%s]",
	},
	EID_VM_SNAP_MERGE: {
		"mid": MOD_WEBUI,
		"formatEN": "VM [%s] merge snap [%s]",
		"formatCN": "虚拟机[%s]回退到snap[%s]",
	},
	EID_VM_SNAP_UPDATE: {
		"mid": MOD_WEBUI,
		"formatEN": "VM [%s] updated snap [%s]",
		"formatCN": "虚拟机[%s]更新snap[%s]",
	},
	EID_VM_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Display VM [%s]",
		"formatCN": "查看虚拟机[%s]",
	},
	EID_VM_SET_CPU: {
		"mid": MOD_WEBUI,
		"formatEN": "SET VM [%s]'s CPU [%d]",
		"formatCN": "设置虚拟机[%s]的CPU为[%d]",
	},
	EID_VM_SET_MEMORY: {
		"mid": MOD_WEBUI,
		"formatEN": "SET VM [%s]'s memory [%d]",
		"formatCN": "设置虚拟机[%s]的内存为[%d]",
	},
	EID_VM_CREATE_TEMPLATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Create template [%s] from VM [%s]",
		"formatCN": "创建虚拟机模板[%s]，源虚拟机[%s]",
	},
	EID_VM_UPDATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Update VM [%s]",
		"formatCN": "更新虚拟机[%s]",
	},
	EID_VM_DISK_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add disk for VM [%s],size [%d]",
		"formatCN": "为虚拟机[%s]创建磁盘，大小[%d]",
	},
	EID_VM_DISK_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "Delete disk [%s] from VM [%s]",
		"formatCN": "从虚拟机[%s]中删除磁盘[%s]",
	},
	EID_VM_CDROM_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add cdrom [%s] for VM [%s]",
		"formatCN": "为虚拟机[%s]添加CDROM",
	},
	EID_VM_CDROM_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "Delete cdrom [%s] from VM [%s]",
		"formatCN": "从虚拟机[%s]中删除CDROM[%s]",
	},
	EID_VM_IF_SET: {
		"mid": MOD_WEBUI,
		"formatEN": "Set vif for VM [%s]",
		"formatCN": "为虚拟机[%s]设置vif[%s]",
	},
	EID_VM_IF_BIND: {
		"mid": MOD_WEBUI,
		"formatEN": "Bind vif for VM [%s]",
		"formatCN": "为虚拟机[%s]绑定vif[%s]",
	},
	EID_VM_IF_RATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Rate vif for VM [%s]",
		"formatCN": "为虚拟机[%s]设置vif[%s]速率",
	},
	EID_VM_IF_VLAN_SET: {
		"mid": MOD_WEBUI,
		"formatEN": "Set vlan for VM [%s]",
		"formatCN": "为虚拟机[%s]设置vlan[%d]",
	},
	EID_VM_IF_CREATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Create vif VM [%s]",
		"formatCN": "为虚拟机[%s]添加vif",
	},
	EID_VM_IF_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "Delete vif [%s] from VM [%s]",
		"formatCN": "从虚拟机[%s]中删除Vif[%s]",
	},
	EID_VM_ISO_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add iso [%s] for VM [%s]",
		"formatCN": "为虚拟机[%s]添加iso[%s]",
	},
	EID_VM_ISO_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "Delete iso [%s] from VM [%s]",
		"formatCN": "从虚拟机[%s]中删除iso[%s]",
	},
	EID_VM_MIGRATE: {
		"mid": MOD_WEBUI,
		"formatEN": "VM [%s] migrate to [%s]",
		"formatCN": "虚拟机[%s]迁移到[%s]",
	},
	EID_VM_CHANGE_OS: {
		"mid": MOD_WEBUI,
		"formatEN": "VM [%s] changeos [%s]",
		"formatCN": "虚拟机[%s]切换操作系统模板为[%s]",
	},
	EID_IPPOOL_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Display IP Pool [%s]",
		"formatCN": "查看IP地址池[%s]",
	},
	EID_IPPOOL_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add IP Pool [%s],start [%s],end [%s],mask [%s],gateway [%s]",
		"formatCN": "添加IP地址池[%s]，开始地址[%s]，结束地址[%s]，掩码[%s]，网关[%s]",
	},
	EID_IPPOOL_UPDATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Update IP Pool [%s],start [%s],end [%s],mask [%s],gateway [%s]",
		"formatCN": "更新IP地址池[%s]，开始地址[%s]，结束地址[%s]，掩码[%s]，网关[%s]",
	},
	EID_IPPOOL_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "Delete IP Pool [%s]",
		"formatCN": "删除IP地址池[%s]",
	},
	EID_VG_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Display VG [%s] of DC [%s]",
		"formatCN": "查看虚拟机分组[%s]，数据中心[%s]",
	},
	EID_VG_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add VG [%s] for DC [%s]",
		"formatCN": "添加虚拟机分组[%s]，数据中心[%s]",
	},
	EID_VG_UPDATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Update VG [%s] for DC [%s]",
		"formatCN": "更新虚拟机分组[%s]，数据中心[%s]",
	},
	EID_VG_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "Delete VG [%s] from DC [%s]",
		"formatCN": "删除虚拟机分组[%s]，数据中心[%s]",
	},
	EID_VG_ALLOWVM: {
		"mid": MOD_WEBUI,
		"formatEN": "Allow vm [%s] for VG [%s]",
		"formatCN": "将虚拟机[%s]添加到虚拟机分组[%s]中",
	},
	EID_VG_DISALLOWVM: {
		"mid": MOD_WEBUI,
		"formatEN": "Disallow vm [%s] for VG [%s]",
		"formatCN": "将虚拟机[%s]从虚拟机分组[%s]中移除",
	},
	EID_VG_BATCH_OPERATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Do [%s] batch operation for VG [%s],VM [%s]",
		"formatCN": "在虚拟机分组[%s]中，执行批量操作[%s]，虚拟机[%s]",
	},
	EID_VG_BATCH_CREATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Do batch create operation for VG [%s],VM name [%s],template [%s],memory [%d],cpu [%d],count [%d]",
		"formatCN": "在虚拟机分组[%s]中，执行批量创建操作，虚拟机名[%s]，模板[%s]，内存[%d]，CPU[%d]，数量[%d]",
	},
	EID_LOG_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Display VG [%s]",
		"formatCN": "查看日志设置",
	},
	EID_LOG_SET: {
		"mid": MOD_WEBUI,
		"formatEN": "Log set,modules [%s],level [%s]",
		"formatCN": "设置日志级别，模块[%s]，级别[%s]",
	},
	EID_STORAGE_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Display storage [%s]",
		"formatCN": "查看存储[%s]",
	},
	EID_STORAGE_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add storage [%s]",
		"formatCN": "添加存储[%s]，类型[%s]，设备[%s]",
	},
	EID_STORAGE_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "Delete storage [%s]",
		"formatCN": "删除存储[%s]",
	},
	EID_TEMPLATE_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Display template [%s]",
		"formatCN": "查看虚拟机模板[%s]",
	},
	EID_TEMPLATE_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add template [%s]",
		"formatCN": "添加虚拟机模板[%s]，大小[%d]，类型[%s]",
	},
	EID_TEMPLATE_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "Delete template [%s]",
		"formatCN": "删除虚拟机模板[%s]",
	},
	EID_TASK_CREATE: {
		"mid": MOD_TASKENGINE,
		"formatEN": "Creat task [%s]:[%s]",
		"formatCN": "创建任务[%s]:[%s]",
	},
	EID_TASK_START: {
		"mid": MOD_TASKENGINE,
		"formatEN": "Start task [%s]:[%s]",
		"formatCN": "启动任务[%s]:[%s]",
	},
	EID_TASK_FINISH: {
		"mid": MOD_TASKENGINE,
		"formatEN": "Run task [%s]:[%s] finished",
		"formatCN": "任务[%s]:[%s]运行结束",
	},
	EID_TASK_RUNNING_IN_SERVER: {
		"mid": MOD_TASKENGINE,
		"formatEN": "Run task [%s]:[%s] finished",
		"formatCN": "任务[%s]:[%s]运行结束，服务器任务[%s]",
	},
	EID_DASHBOARD_CPU: {
		"mid": MOD_WEBUI,
		"formatEN": "Dashboard get CPU info",
		"formatCN": "仪表盘获取CPU信息",
	},
	EID_DASHBOARD_RRDCPU: {
		"mid": MOD_WEBUI,
		"formatEN": "Dashboard get RRD CPU info",
		"formatCN": "仪表盘获取RRDCPU信息",
	},
	EID_DASHBOARD_MEMORY: {
		"mid": MOD_WEBUI,
		"formatEN": "Dashboard get memory info",
		"formatCN": "仪表盘获取内存信息",
	},
	EID_DASHBOARD_RRDMEMORY: {
		"mid": MOD_WEBUI,
		"formatEN": "Dashboard get RRD memory info",
		"formatCN": "仪表盘获取RRD内存信息",
	},
	EID_DASHBOARD_MEMORYVM: {
		"mid": MOD_WEBUI,
		"formatEN": "Dashboard get memory vm info",
		"formatCN": "仪表盘获取主机内存信息",
	},
	EID_DASHBOARD_LICENSE: {
		"mid": MOD_WEBUI,
		"formatEN": "Dashboard get license info",
		"formatCN": "仪表盘获取许可信息",
	},
	EID_DASHBOARD_HOSTVM: {
		"mid": MOD_WEBUI,
		"formatEN": "Dashboard get host vm info",
		"formatCN": "仪表盘获取主机上虚拟机信息",
	},
	EID_DASHBOARD_STORAGE: {
		"mid": MOD_WEBUI,
		"formatEN": "Dashboard get storage info",
		"formatCN": "仪表盘获取存储信息",
	},
	EID_DASHBOARD_STORAGEVM: {
		"mid": MOD_WEBUI,
		"formatEN": "Dashboard get storage vm info",
		"formatCN": "仪表盘获取存储上虚拟机信息",
	},
	EID_DNS_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Get DNS info",
		"formatCN": "查询DNS信息",
	},
	EID_DNS_SET: {
		"mid": MOD_WEBUI,
		"formatEN": "Set DNS info[%s]",
		"formatCN": "设置DNS信息，地址：%s",
	},
	EID_HA_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Get HA info,hostpool:%s,storage:%s",
		"formatCN": "查询HA信息，主机池：%s，存储：%s",
	},
	EID_HA_SET_STATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Get HA info,hostpool:%s,storage:%s",
		"formatCN": "查询HA信息，主机池：%s，存储：%s",
	},
	EID_HA_SET_CONFIG: {
		"mid": MOD_WEBUI,
		"formatEN": "Get HA info,hostpool:%s,storage:%s",
		"formatCN": "查询HA信息，主机池：%s，存储：%s",
	},
	EID_HA_PROPOSE_MASTER: {
		"mid": MOD_WEBUI,
		"formatEN": "Get HA info,hostpool:%s,storage:%s",
		"formatCN": "查询HA信息主机池：%s，存储：%s",
	},
	EID_HA_EXCLUDE: {
		"mid": MOD_WEBUI,
		"formatEN": "Get HA info,hostpool:%s,storage:%s",
		"formatCN": "查询HA信息，主机池：%s，存储：%s",
	},
	EID_NETWORK_INTERFACE_GET_LIST: {
		"mid": MOD_WEBUI,
		"formatEN": "Get interface list",
		"formatCN": "查询网卡列表",
	},
	EID_NETWORK_INTERFACE_GET_INFO: {
		"mid": MOD_WEBUI,
		"formatEN": "Get interface info,interface name %s",
		"formatCN": "查询网卡信息，接口名%s",
	},
	EID_NETWORK_INTERFACE_SET_CONFIG: {
		"mid": MOD_WEBUI,
		"formatEN": "Set interface config,interface name %s,addr %s,netmask %s",
		"formatCN": "设置网卡信息，接口名：%s，地址：%s，掩码：%s",
	},
	EID_NETWORK_INTERFACE_DEL: {
		"mid": MOD_WEBUI,
		"formatEN": "Delete interface config,interface name %s",
		"formatCN": "删除网卡信息，接口名：%s",
	},
	EID_NETWORK_ROUTE_GET_LIST: {
		"mid": MOD_WEBUI,
		"formatEN": "Get route list",
		"formatCN": "查询路由信息",
	},
	EID_NETWORK_ROUTE_SET: {
		"mid": MOD_WEBUI,
		"formatEN": "Set route into,dest %s/%s,gateway %s",
		"formatCN": "设置路由信息，目的：%s/%s，网关：%s",
	},
	EID_NETWORK_ROUTE_DEL: {
		"mid": MOD_WEBUI,
		"formatEN": "Delete route into,dest %s/%s,gateway %s",
		"formatCN": "删除路由信息，目的：%s/%s，网关：%s",
	},
	EID_SYSTEM_LICENSE_UPLOAD: {
		"mid": MOD_WEBUI,
		"formatEN": "upload license file %s",
		"formatCN": "上传许可文件：%s",
	},
	EID_LOGS_SET_LOG_LEVEL: {
		"mid": MOD_WEBUI,
		"formatEN": "Set log level,module %s,level %s",
		"formatCN": "设置日志级别，模块：%s，级别：%s",
	},
	EID_LOGS_SET_DEBUG_LEVEL: {
		"mid": MOD_WEBUI,
		"formatEN": "Set debug level,module %s,level %s",
		"formatCN": "设置调试级别，模块：%s，级别：%s",
	},
	EID_LOGS_SET_APIRECORD_STATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Set api record state to %s",
		"formatCN": "设置API记录状态：%s",
	},
	EID_LOGS_SET_REMOTE_LOG: {
		"mid": MOD_WEBUI,
		"formatEN": "Set remote log %s",
		"formatCN": "设置日志远程发送：%s",
	},
	EID_PATCH_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Get system patches",
		"formatCN": "查询系统补丁",
	},
	EID_PATCH_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add system patch %s",
		"formatCN": "添加系统补丁：%s",
	},
	EID_PATCH_DEL: {
		"mid": MOD_WEBUI,
		"formatEN": "Delete system patch %s",
		"formatCN": "删除系统补丁：%s",
	},
	EID_PATCH_SET_STATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Set system patch %s state to %s",
		"formatCN": "设置系统补丁：%s，状态为：%s",
	},
	EID_PATCH_SYSTEM_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Get system package",
		"formatCN": "查询系统包信息",
	},
	EID_PATCH_SYSTEM_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Install system package %s",
		"formatCN": "安装系统升级包：%s",
	},
	EID_PATCH_SERVER_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Get server package list",
		"formatCN": "查询Server端系统包列表",
	},
	EID_PATCH_SERVER_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add server package %s",
		"formatCN": "添加Server系统包：%s",
	},
	EID_PATCH_SERVER_DEL: {
		"mid": MOD_WEBUI,
		"formatEN": "Delete server package %s",
		"formatCN": "删除Server系统包：%s",
	},
	EID_PATCH_SERVER_UPGRADE: {
		"mid": MOD_WEBUI,
		"formatEN": "Update server package %s %s",
		"formatCN": "使用升级包[%s]升级Server[%s]",
	},
	EID_ALARM_TYPE_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Get alarm type info",
		"formatCN": "查询报警类型信息",
	},
	EID_ALARM_METHOD_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Get alarm method info",
		"formatCN": "查询报警方式信息",
	},
	EID_ALARM_METHOD_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add alarm method",
		"formatCN": "添加报警方式信息",
	},
	EID_ALARM_METHOD_UPDATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Update alarm method",
		"formatCN": "编辑报警方式信息",
	},
	EID_ALARM_METHOD_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "Delete alarm method",
		"formatCN": "删除报警方式信息",
	},
	EID_ALARM_RULE_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Get alarm rule info",
		"formatCN": "查询报警规则信息",
	},
	EID_ALARM_RULE_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add alarm rule",
		"formatCN": "添加报警规则信息",
	},
	EID_ALARM_RULE_UPDATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Update alarm rule",
		"formatCN": "编辑报警规则信息",
	},
	EID_ALARM_RULE_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "Delete alarm rule",
		"formatCN": "删除报警规则信息",
	},
	EID_PROCESS_STATUS_CHANGES: {
		"mid": MOD_WEBUI,
		"formatEN": "Process status changes",
		"formatCN": "进程状态变更",
	},
	EID_CLIENTPOLICY_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add ClientPolicy [%s]",
		"formatCN": "添加客户端安全策略[%s]",
	},
	EID_CLIENTPOLICY_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "ClientPolicy [%s] delete",
		"formatCN": "删除客户端安全策略[%s]",
	},
	EID_CLIENTPOLICY_UPDATE: {
		"mid": MOD_WEBUI,
		"formatEN": "ClientPolicy [%s] update",
		"formatCN": "客户端安全策略[%s]成功更新",
	},
	EID_CLIENTPOLICY_DSIPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Display ClientPolicy[%s]",
		"formatCN": "查询客户端安全策略[%s]",
	},
	EID_USERGROUP_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add UserGroup [%s]",
		"formatCN": "添加终端用户组[%s]",
	},
	EID_USERGROUP_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "UserGroup [%s] delete",
		"formatCN": "删除终端用户组[%s]",
	},
	EID_USERGROUP_UPDATE: {
		"mid": MOD_WEBUI,
		"formatEN": "UserGroup [%s] update",
		"formatCN": "终端用户组[%s]成功更新",
	},
	EID_USERGROUP_DSIPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Display UserGroup [%s]",
		"formatCN": "查询终端用户组[%s]",
	},
	EID_USERGROUP_BINDUSER: {
		"mid": MOD_WEBUI,
		"formatEN": "UserGroup [%s] binduser",
		"formatCN": "终端用户组[%s]绑定用户",
	},
	EID_USERGROUP_BINDCLIENTPOLICY: {
		"mid": MOD_WEBUI,
		"formatEN": "UserGroup [%s] bindclientpolicy",
		"formatCN": "终端用户组[%s]绑定客户端策略",
	},
	EID_VMOFFERING_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add vm offering [%s]",
		"formatCN": "添加计算规格[%s]",
	},
	EID_VMOFFERING_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "Delelte vm offering [%s]",
		"formatCN": "删除计算规格[%s]",
	},
	EID_VMOFFERING_UPDATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Update vm offering [%s]",
		"formatCN": "修改计算规格[%s]",
	},
	EID_VMOFFERING_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Display all vm offering",
		"formatCN": "获取所有计算规格",
	},
	EID_DISKOFFERING_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add disk offering [%s]",
		"formatCN": "添加云盘规格[%s]",
	},
	EID_DISKOFFERING_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "Delelte disk offering [%s]",
		"formatCN": "删除云盘规格[%s]",
	},
	EID_DISKOFFERING_UPDATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Update disk offering [%s]",
		"formatCN": "修改云盘规格[%s]",
	},
	EID_DISKOFFERING_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Display all disk offering",
		"formatCN": "获取所有云盘规格",
	},
	EID_VROFFERING_ADD: {
		"mid": MOD_WEBUI,
		"formatEN": "Add vr offering [%s]",
		"formatCN": "添加虚拟路由规格[%s]",
	},
	EID_VROFFERING_DELETE: {
		"mid": MOD_WEBUI,
		"formatEN": "Delelte vr offering [%s]",
		"formatCN": "删除虚拟路由规格[%s]",
	},
	EID_VROFFERING_UPDATE: {
		"mid": MOD_WEBUI,
		"formatEN": "Update vr offering [%s]",
		"formatCN": "修改虚拟路由规格[%s]",
	},
	EID_VROFFERING_DISPLAY: {
		"mid": MOD_WEBUI,
		"formatEN": "Display all vr offering",
		"formatCN": "获取所有虚拟路由规格",
	},
}

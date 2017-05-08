#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

DB_USER = "root"
DB_PASSWORD = "123456"
DB_NAME = "dbrobot"

UNIXSOCKET_DEBIAN = "/var/run/mysqld/mysqld.sock"
UNIXSOCKET_REDCENT = "/var/lib/mysql/mysql.sock"

DB_SERVER = "127.0.0.1"

TB_ACCOUNT = "tb_account"
TB_MISC = "tb_misc"
TB_LOG = "tb_log"
TB_APIRECORD = "tb_apirecord"
TB_APITRACE = "tb_apitrace"
TB_SESSION = "tb_session"
TB_USER = "tb_user"


def get_sock_file():
	if (os.path.exists(UNIXSOCKET_DEBIAN)):
		return UNIXSOCKET_DEBIAN
	else:
		return UNIXSOCKET_REDCENT

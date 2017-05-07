DROP TABLE IF EXISTS `tb_log`;
CREATE TABLE `tb_log` (
		`TIME` BIGINT NOT NULL DEFAULT '0',
		`USER` VARCHAR(64) NOT NULL DEFAULT 'none',
		`EID` BIGINT NOT NULL DEFAULT '0',
		`MODULE` VARCHAR(32) NOT NULL DEFAULT '',
		`PRI` TINYINT NOT NULL DEFAULT 5,
		`MSG` VARCHAR(1024) NOT NULL DEFAULT ''
) ENGINE=Innodb DEFAULT CHARSET=utf8;
ALTER TABLE tb_log ADD INDEX tb_log_time (TIME);
ALTER TABLE tb_log ADD INDEX tb_log_eid (EID);
ALTER TABLE tb_log ADD INDEX tb_log_user (USER);
ALTER TABLE tb_log ADD INDEX tb_log_module (MODULE);
ALTER TABLE tb_log ADD INDEX tb_log_moduleeid (MODULE, EID);
ALTER TABLE tb_log ADD INDEX tb_log_pri (PRI);

DROP TABLE IF EXISTS `tb_apirecord`;
CREATE TABLE `tb_apirecord` (
		`ID` BIGINT NOT NULL AUTO_INCREMENT,
		`TIME` BIGINT NOT NULL DEFAULT '0',
		`USER` VARCHAR(128) NOT NULL DEFAULT 'none',
		`URL` VARCHAR(1024) NOT NULL DEFAULT '',
		`PARAS` TEXT NOT NULL DEFAULT '',
		`RESULT` TEXT NOT NULL DEFAULT '',
		PRIMARY KEY (`ID`)
) ENGINE=Innodb DEFAULT CHARSET=utf8;
ALTER TABLE tb_apirecord ADD INDEX tb_apirecord_id (ID);
ALTER TABLE tb_apirecord ADD INDEX tb_apirecord_time (TIME);
ALTER TABLE tb_apirecord ADD INDEX tb_apirecord_user (USER);

DROP TABLE IF EXISTS `tb_account`;
CREATE TABLE `tb_account` (
		`ID` VARCHAR(36) NOT NULL DEFAULT '',
		`U_State` TINYINT NOT NULL DEFAULT '1' COMMENT '1: OK, 0: Bad',
		`U_Type` INTEGER NOT NULL DEFAULT '3' COMMENT '7: super,3 admin,1 audit',
		`U_Name` VARCHAR(128) NOT NULL DEFAULT '',
		`U_QuotaId` VARCHAR(36) NOT NULL DEFAULT '',
		`U_UKey` VARCHAR(36) NOT NULL DEFAULT '' COMMENT 'UKEY Id',
		`U_Password` VARCHAR(128) NOT NULL DEFAULT '',
		`U_Email` VARCHAR(128) NOT NULL DEFAULT '',
		`U_PhoneNumber` VARCHAR(32) NOT NULL DEFAULT '',
		`U_LastLogin` BIGINT NOT NULL DEFAULT '0',
		`U_CreateTime` BIGINT NOT NULL DEFAULT '0',
		`U_LastSync` BIGINT NOT NULL DEFAULT '0',
		`U_Description` VARCHAR(1024) NOT NULL DEFAULT '',
		PRIMARY KEY (`ID`)
) ENGINE=Innodb DEFAULT CHARSET=utf8;
ALTER TABLE tb_account ADD INDEX tb_account_id (ID);
ALTER TABLE tb_account ADD INDEX tb_account_state (U_State);
ALTER TABLE tb_account ADD INDEX tb_account_name (U_Name);
ALTER TABLE tb_account ADD INDEX tb_account_type (U_Type);
ALTER TABLE tb_account ADD INDEX tb_account_ukey (U_UKey);
ALTER TABLE tb_account ADD INDEX tb_account_email (U_Email);
ALTER TABLE tb_account ADD INDEX tb_account_phonenumber (U_PhoneNumber);
ALTER TABLE tb_account ADD INDEX tb_account_password (U_Password);
ALTER TABLE tb_account ADD INDEX tb_account_createtime (U_CreateTime);
ALTER TABLE tb_account ADD INDEX tb_account_lastlogin (U_LastLogin);
ALTER TABLE tb_account ADD INDEX tb_account_lastsync (U_LastSync);

DROP TABLE IF EXISTS `tb_user`;
CREATE TABLE `tb_user` (
		`ID` VARCHAR(36) NOT NULL DEFAULT '',
		`U_Name` VARCHAR(128) NOT NULL DEFAULT '',
		`U_State` TINYINT NOT NULL DEFAULT '1' COMMENT '1: OK, 0: Bad',
		`U_Type` INTEGER NOT NULL DEFAULT '0' COMMENT '0 for terminal user',
		`U_LastLogin` BIGINT NOT NULL DEFAULT '0',
		`U_LastSync` BIGINT NOT NULL DEFAULT '0',
		`U_CreateTime` BIGINT NOT NULL DEFAULT '0',
		`U_Password` VARCHAR(128) NOT NULL DEFAULT '',
		`U_Email` VARCHAR(128) NOT NULL DEFAULT '',
		`U_UKey` VARCHAR(36) NOT NULL DEFAULT '' COMMENT 'UKEY Id',
		`U_VmPassword` VARCHAR(1024) NOT NULL DEFAULT '',
		`U_PhoneNumber` VARCHAR(32) NOT NULL DEFAULT '',
		`U_Description` VARCHAR(1024) NOT NULL DEFAULT '',
		PRIMARY KEY (`ID`)
) ENGINE=Innodb DEFAULT CHARSET=utf8;
ALTER TABLE tb_user ADD INDEX tb_user_id (ID);
ALTER TABLE tb_user ADD INDEX tb_user_state (U_State);
ALTER TABLE tb_user ADD INDEX tb_user_name (U_Name);
ALTER TABLE tb_user ADD INDEX tb_user_type (U_Type);
ALTER TABLE tb_user ADD INDEX tb_user_email (U_Email);
ALTER TABLE tb_user ADD INDEX tb_user_ukey (U_UKey);
ALTER TABLE tb_user ADD INDEX tb_user_phonenumber (U_PhoneNumber);
ALTER TABLE tb_user ADD INDEX tb_user_password (U_Password);
ALTER TABLE tb_user ADD INDEX tb_user_createtime (U_CreateTime);
ALTER TABLE tb_user ADD INDEX tb_user_lastlogin (U_LastLogin);
ALTER TABLE tb_user ADD INDEX tb_user_lastsync (U_LastSync);

DROP TABLE IF EXISTS `tb_session`;
CREATE TABLE `tb_session` (
		`ID` VARCHAR(36) NOT NULL DEFAULT '',
		`S_UserId` VARCHAR(36) NOT NULL DEFAULT '',
		`S_UserType` TINYINT NOT NULL DEFAULT '0' COMMENT '7:superadmin,3:admin,1:audit,0:user,11:classadmin,12:teacher',
		`S_UserName` VARCHAR(128) NOT NULL DEFAULT '',
		`S_Cookie` VARCHAR(1024) NOT NULL DEFAULT '',
		`S_CreateTime` BIGINT NOT NULL DEFAULT '0',
		`S_LastSync` BIGINT NOT NULL DEFAULT '0',
		`S_ExpireTime` BIGINT NOT NULL DEFAULT '0',
		PRIMARY KEY (`ID`)
) ENGINE=Innodb DEFAULT CHARSET=utf8;
ALTER TABLE tb_session ADD INDEX tb_session_id (ID);
ALTER TABLE tb_session ADD INDEX tb_session_userid (S_UserId);
ALTER TABLE tb_session ADD INDEX tb_session_username (S_UserName);
ALTER TABLE tb_session ADD INDEX tb_session_createtime (S_CreateTime);
ALTER TABLE tb_session ADD INDEX tb_session_lastsync (S_LastSync);
ALTER TABLE tb_session ADD INDEX tb_session_expiretime (S_ExpireTime);

DROP TABLE IF EXISTS `tb_misc`;
CREATE TABLE `tb_misc` (
		`ID` BIGINT NOT NULL AUTO_INCREMENT,
		`M_Name` VARCHAR(64) NOT NULL DEFAULT '',
		`M_Value` VARCHAR(64) NOT NULL DEFAULT '',
		`M_Type` VARCHAR(64) NOT NULL DEFAULT '',
		PRIMARY KEY (`ID`)
) ENGINE=Innodb DEFAULT CHARSET=utf8;
ALTER TABLE tb_misc ADD INDEX tb_misc_id (ID);
ALTER TABLE tb_misc ADD INDEX tb_misc_name (M_Name);

DROP TABLE IF EXISTS `tb_apitrace`;
CREATE TABLE `tb_apitrace` (
		`ID` VARCHAR(36) NOT NULL DEFAULT '',
		`AT_AccountId` VARCHAR(36) NOT NULL DEFAULT '',
		`AT_Type` VARCHAR(16) NOT NULL DEFAULT 'api' COMMENT 'api or task',
		`AT_ApiId` VARCHAR(200) NOT NULL DEFAULT '',
		`AT_State` VARCHAR(16) NOT NULL DEFAULT 'New' COMMENT 'New,Loaded,Running,ServerRunning,Failed,Finished',
		`AT_Name` VARCHAR(128) NOT NULL DEFAULT '',
		`AT_CreateTime` BIGINT NOT NULL DEFAULT '0',
		`AT_StartTime` BIGINT NOT NULL DEFAULT '0',
		`AT_FinishTime` BIGINT NOT NULL DEFAULT '0',
		`AT_User` VARCHAR(64) NOT NULL DEFAULT '',
		`AT_ServerTaskId` VARCHAR(36) NOT NULL DEFAULT '',
		`AT_Request` VARCHAR(8192) NOT NULL DEFAULT '{}',
		`AT_ServerRequest` VARCHAR(8192) NOT NULL DEFAULT '{}',
		`AT_Reply` TEXT NOT NULL,
		PRIMARY KEY (`ID`)
) ENGINE=Innodb DEFAULT CHARSET=utf8;
ALTER TABLE tb_apitrace ADD INDEX tb_apitrace_id (ID);
ALTER TABLE tb_apitrace ADD INDEX tb_apitrace_type (AT_Type);
ALTER TABLE tb_apitrace ADD INDEX tb_apitrace_apiid (AT_ApiId);
ALTER TABLE tb_apitrace ADD INDEX tb_apitrace_staskid (AT_ServerTaskId);
ALTER TABLE tb_apitrace ADD INDEX tb_apitrace_user (AT_User);
ALTER TABLE tb_apitrace ADD INDEX tb_apitrace_accountId (AT_AccountId);
ALTER TABLE tb_apitrace ADD INDEX tb_apitrace_createtime (AT_CreateTime);
ALTER TABLE tb_apitrace ADD INDEX tb_apitrace_finishtime (AT_FinishTime);
ALTER TABLE tb_apitrace ADD INDEX tb_apitrace_starttime (AT_StartTime);

DROP TRIGGER IF EXISTS trigger_delete_session;
DROP TRIGGER IF EXISTS trigger_delete_user;
DROP TRIGGER IF EXISTS trigger_delete_account;

DELIMITER //

CREATE TRIGGER trigger_delete_user AFTER DELETE ON tb_user FOR EACH ROW
BEGIN
END; //

CREATE TRIGGER trigger_delete_account AFTER DELETE ON tb_account FOR EACH ROW
BEGIN
DELETE FROM tb_session WHERE S_UserId=old.ID;
END; //

CREATE TRIGGER trigger_delete_session AFTER DELETE ON tb_session FOR EACH ROW 
BEGIN
END; //

DELIMITER ;

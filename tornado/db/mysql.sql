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

DROP TABLE IF EXISTS `tb_account`;
CREATE TABLE `tb_account` (
		`ID` VARCHAR(36) NOT NULL DEFAULT '',
		`U_State` TINYINT NOT NULL DEFAULT '1' COMMENT '1: OK, 0: BAD',
		`U_Type` INTEGER NOT NULL DEFAULT '3' COMMENT '7: super,3 admin,1 audit',
		`U_Name` VARCHAR(128) NOT NULL DEFAULT '',
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
ALTER TABLE tb_account ADD INDEX tb_account_email (U_Email);
ALTER TABLE tb_account ADD INDEX tb_account_password (U_Password);
ALTER TABLE tb_account ADD INDEX tb_account_createtime (U_CreateTime);
ALTER TABLE tb_account ADD INDEX tb_account_lastlogin (U_LastLogin);
ALTER TABLE tb_account ADD INDEX tb_account_lastsync (U_LastSync);


DROP TABLE IF EXISTS `tb_quota`;
CREATE TABLE `tb_quota` (
		`ID` VARCHAR(36) NOT NULL DEFAULT '',
		`Q_Name` VARCHAR(64) NOT NULL DEFAULT '',
		`Q_AccountId` VARCHAR(36) NOT NULL DEFAULT '',
		`Q_Robot` INTEGER NOT NULL DEFAULT '0',
		`Q_Message` INTEGER NOT NULL DEFAULT '0' COMMENT 'Message Amount in MB',
		`Q_Group` INTEGER NOT NULL DEFAULT '0' COMMENT 'Group Amount',
		`Q_CreateTime` BIGINT NOT NULL DEFAULT '0',
		`Q_LastSync` BIGINT NOT NULL DEFAULT '0',
		PRIMARY KEY (`ID`)
) ENGINE=Innodb DEFAULT CHARSET=utf8;
ALTER TABLE tb_quota ADD INDEX tb_quota_id (ID);
ALTER TABLE tb_quota ADD INDEX tb_quota_name (Q_Name);
ALTER TABLE tb_quota ADD INDEX tb_quota_accountid (Q_AccountId);


DROP TABLE IF EXISTS `tb_robot`;
CREATE TABLE `tb_robot` (
		`ID` VARCHAR(36) NOT NULL DEFAULT '',
		`R_AccountId` VARCHAR(128) NOT NULL DEFAULT '',
		`R_Name` VARCHAR(128) NOT NULL DEFAULT '' COMMENT 'Robot Name',
		`R_UName` VARCHAR(128) NOT NULL DEFAULT '' COMMENT 'WeChat Name',
		`R_UId` VARCHAR(128) NOT NULL DEFAULT '',
		`R_State` TINYINT NOT NULL DEFAULT '0' COMMENT '1: ONLINE, 0: OFFLINE, 2: WAITING_SCAN',
		`R_LastLogin` BIGINT NOT NULL DEFAULT '0',
		`R_LastSync` BIGINT NOT NULL DEFAULT '0',
		`R_CreateTime` BIGINT NOT NULL DEFAULT '0',
		`R_Description` VARCHAR(1024) NOT NULL DEFAULT '',
		PRIMARY KEY (`ID`)
) ENGINE=Innodb DEFAULT CHARSET=utf8;
ALTER TABLE tb_robot ADD INDEX tb_robot_id (ID);
ALTER TABLE tb_robot ADD INDEX tb_robot_uid (R_UId);
ALTER TABLE tb_robot ADD INDEX tb_robot_accountid (R_AccountId);
ALTER TABLE tb_robot ADD INDEX tb_robot_state (R_State);
ALTER TABLE tb_robot ADD INDEX tb_robot_name (R_Name);
ALTER TABLE tb_robot ADD INDEX tb_robot_createtime (R_CreateTime);
ALTER TABLE tb_robot ADD INDEX tb_robot_lastlogin (R_LastLogin);
ALTER TABLE tb_robot ADD INDEX tb_robot_lastsync (R_LastSync);


DROP TABLE IF EXISTS `tb_contact`;
CREATE TABLE `tb_contact` (
		`ID` VARCHAR(36) NOT NULL DEFAULT '',
		`C_RobotId` VARCHAR(36) NOT NULL DEFAULT '',
 		`C_UserName` VARCHAR(128) NOT NULL DEFAULT '',
 		`C_HeadImgUrl` VARCHAR(1024) NOT NULL DEFAULT '',
 		`C_ContactFlag` TINYINT NOT NULL DEFAULT '3' COMMENT '3: common,',
		`C_NickName` VARCHAR(128) NOT NULL DEFAULT '',
		`C_Alias` VARCHAR(128) NOT NULL DEFAULT '',
		`C_Signature` VARCHAR(256) NOT NULL DEFAULT '' COMMENT '',
		`C_Province` VARCHAR(32) NOT NULL DEFAULT '' COMMENT '',
		`C_City` VARCHAR(32) NOT NULL DEFAULT '',
		`C_Raw` VARCHAR(4096) NOT NULL DEFAULT '{}',
		`C_Sex` TINYINT NOT NULL DEFAULT '0' COMMENT '1: Male, 2: Female, 0: Unknown',
		`C_LastSync` BIGINT NOT NULL DEFAULT '0',
		`C_CreateTime` BIGINT NOT NULL DEFAULT '0',
		PRIMARY KEY (`ID`)
) ENGINE=Innodb DEFAULT CHARSET=utf8;
ALTER TABLE tb_contact ADD INDEX tb_robot_id (ID);
ALTER TABLE tb_contact ADD INDEX tb_contact_robotid (C_RobotId);
ALTER TABLE tb_contact ADD INDEX tb_contact_username (C_UserName);
ALTER TABLE tb_contact ADD INDEX tb_contact_sex (C_Sex);
ALTER TABLE tb_contact ADD INDEX tb_contact_createtime (C_CreateTime);
ALTER TABLE tb_contact ADD INDEX tb_contact_lastsync (C_LastSync);



DROP TABLE IF EXISTS `tb_session`;
CREATE TABLE `tb_session` (
		`ID` VARCHAR(36) NOT NULL DEFAULT '',
		`S_UserId` VARCHAR(36) NOT NULL DEFAULT '',
		`S_UserType` TINYINT NOT NULL DEFAULT '3' COMMENT '7:superadmin,3:admin',
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
		`AT_State` VARCHAR(16) NOT NULL DEFAULT 'New' COMMENT 'New,Loaded,Running,Failed,Finished',
		`AT_Name` VARCHAR(128) NOT NULL DEFAULT '',
		`AT_CreateTime` BIGINT NOT NULL DEFAULT '0',
		`AT_StartTime` BIGINT NOT NULL DEFAULT '0',
		`AT_FinishTime` BIGINT NOT NULL DEFAULT '0',
		`AT_User` VARCHAR(64) NOT NULL DEFAULT '',
		`AT_Request` VARCHAR(8192) NOT NULL DEFAULT '{}',
		`AT_Reply` TEXT NOT NULL,
		PRIMARY KEY (`ID`)
) ENGINE=Innodb DEFAULT CHARSET=utf8;
ALTER TABLE tb_apitrace ADD INDEX tb_apitrace_id (ID);
ALTER TABLE tb_apitrace ADD INDEX tb_apitrace_type (AT_Type);
ALTER TABLE tb_apitrace ADD INDEX tb_apitrace_apiid (AT_ApiId);
ALTER TABLE tb_apitrace ADD INDEX tb_apitrace_user (AT_User);
ALTER TABLE tb_apitrace ADD INDEX tb_apitrace_accountId (AT_AccountId);
ALTER TABLE tb_apitrace ADD INDEX tb_apitrace_createtime (AT_CreateTime);
ALTER TABLE tb_apitrace ADD INDEX tb_apitrace_finishtime (AT_FinishTime);
ALTER TABLE tb_apitrace ADD INDEX tb_apitrace_starttime (AT_StartTime);

DROP TRIGGER IF EXISTS trigger_delete_session;
DROP TRIGGER IF EXISTS trigger_delete_user;
DROP TRIGGER IF EXISTS trigger_delete_account;

DELIMITER //

CREATE TRIGGER trigger_delete_robot AFTER DELETE ON tb_robot FOR EACH ROW
BEGIN
END; //

CREATE TRIGGER trigger_delete_account AFTER DELETE ON tb_account FOR EACH ROW
BEGIN
DELETE FROM tb_session WHERE S_UserId=old.ID;
DELETE FROM tb_quota WHERE Q_AccountId=old.ID;
END; //

CREATE TRIGGER trigger_delete_session AFTER DELETE ON tb_session FOR EACH ROW 
BEGIN
END; //

DELIMITER ;

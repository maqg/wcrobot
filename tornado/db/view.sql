DROP VIEW IF EXISTS v_user;
CREATE VIEW v_user (ID,Name) 
	as SELECT ID,U_Name FROM tb_user;

DROP VIEW IF EXISTS v_account;
CREATE VIEW v_account (ID,Name) 
	as SELECT ID,U_Name FROM tb_account;

DROP VIEW IF EXISTS v_robot;
CREATE VIEW v_robot (ID,Name) 
	as SELECT ID,R_Name FROM tb_robot;

DROP VIEW IF EXISTS v_account;
CREATE VIEW v_account (ID,Name) 
	as SELECT ID,U_Name FROM tb_account;

/*Write a trigger to insert the existing values of the EMP table into NEWEMP table when the record is deleted from EMP table.*/

SET SERVEROUTPUT ON
SET FEEDBACK OFF
SET VERIFY OFF

CREATE OR REPLACE TRIGGER TRG_DEL_BACKUP
BEFORE DELETE
ON EMP
FOR EACH ROW
BEGIN
	INSERT INTO NEWEMP(EMP_NO,SAL,DEPTNO,EMP_NAME) VALUES(:OLD.EMP_NO,:OLD.SAL,:OLD.DEPTNO,:OLD.EMP_NAME);
END;
/

SET SERVEROUTPUT OFF
SET FEEDBACK ON
SET VERIFY ON
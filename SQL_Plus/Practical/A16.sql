/*Write a trigger to restrict user form using the table on Sunday.*/

SET SERVEROUTPUT ON
SET FEEDBACK OFF
SET VERIFY OFF

CREATE OR REPLACE TRIGGER TRG_SUNDAY
BEFORE INSERT OR UPDATE OR DELETE 
ON EMP
FOR EACH ROW

BEGIN
	IF TRIM(TO_CHAR(SYSDATE,'DAY'))='SUNDAY' THEN
		RAISE_APPLICATION_ERROR (-20420,'YOU CAN NOT MODIFY DATA ON SUNDAY');
	END IF;
END;
/

SET SERVEROUTPUT OFF
SET FEEDBACK ON
SET VERIFY ON 
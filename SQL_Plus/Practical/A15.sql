/*Write a trigger that identifies the gender of the employee and according to the gender sets MR. in front of MALE employees and MS. in front of FEMALE employee.*/

SET SERVEROUTPUT ON
SET FEEDBACK OFF
SET VERIFY OFF

CREATE OR REPLACE TRIGGER TRG_GENDER
BEFORE INSERT OR UPDATE 
ON EMP
FOR EACH ROW
BEGIN

	IF :NEW.GENDER = 'MALE' THEN
		:NEW.EMP_NAME := 'MR.'||:NEW.EMP_NAME;
	ELSE
		:NEW.EMP_NAME := 'MS.'||:NEW.EMP_NAME;
	END IF;
END;
/

SET SERVEROUTPUT OFF
SET FEEDBACK ON
SET VERIFY ON
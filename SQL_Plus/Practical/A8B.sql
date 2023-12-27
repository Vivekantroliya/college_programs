/*Write a procedure that search's whether the given employee number is present or not in the table. (Use both IN and OUT mode variables) and also Write a PL/SQL block to call the SEARCH_EMP procedure.*/

SET SERVEROUTPUT ON
SET FEEDBACK OFF
SET VERIFY OFF

DECLARE
	ENAME EMP.EMP_NAME%TYPE;
BEGIN
	EXIST_EMPLOYEE(10,ENAME);
	DBMS_OUTPUT.PUT_LINE('EMPLOYEE NAME IS '||ENAME||'.');
END;
/

SET SERVEROUTPUT OFF
SET FEEDBACK ON
SET VERIFY ON
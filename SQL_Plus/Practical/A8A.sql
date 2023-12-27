/*Write a procedure that search's whether the given employee number is present or not in the table. (Use both IN and OUT mode variables) and also Write a PL/SQL block to call the SEARCH_EMP procedure.*/

SET SERVEROUTPUT ON
SET FEEDBACK OFF
SET VERIFY OFF

CREATE OR REPLACE PROCEDURE EXIST_EMPLOYEE
(EMPNO IN EMP.EMP_NO%TYPE,EXIST_EMP OUT EMP.EMP_NAME%TYPE)
IS
BEGIN
	SELECT EMP_NAME INTO EXIST_EMP FROM EMP WHERE EMP_NO = EMPNO ;
END;
/


SET SERVEROUTPUT OFF
SET FEEDBACK ON
SET VERIFY ON


/*Write a simple procedure that increases by the salary of employees for the given department no by percentage inputted by the user using IN parameter.*/

SET SERVEROUTPUT ON
SET FEEDBACK OFF
SET VERIFY OFF

CREATE OR REPLACE PROCEDURE UPDATE_EMP1(V_DEPTNO IN EMP.DEPTNO%TYPE,V_PERC IN NUMBER)
AS
BEGIN
	UPDATE EMP SET SAL = SAL + (SAL*V_PERC/100) WHERE DEPTNO = V_DEPTNO;
	
END;
/

SET SERVEROUTPUT OFF
SET FEEDBACK ON
SET VERIFY ON
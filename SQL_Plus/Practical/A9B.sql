/*Write a function that returns the square of the given number. Execute this function using separate PL/SQL block and also without using PL/SQL block on command line.*/

SET SERVEROUTPUT ON
SET FEEDBACK OFF
SET VERIFY OFF

DECLARE 
	NUM NUMBER;
	NUM1 NUMBER;
BEGIN
	NUM := &NUMBER;
	NUM1 := SQUARE(NUM);
	DBMS_OUTPUT.PUT_LINE('THE SQUARE OF '||NUM||' IS '||NUM1);
END;
/

SET SERVEROUTPUT OFF
SET FEEDBACK ON
SET VERIFY ON
-- Write a program to calculate the square and cube of the given number.

SET SERVEROUTPUT ON
ACCEPT NUMBER PROMPT "Enter Value Of Number For Square And Cube : "

DECLARE
	NO NUMBER(5);
	NO1 NUMBER(5);
	NO2 NUMBER(5);
BEGIN
	NO := &NUMBER ;
	NO1 := POWER(NO,2);
	NO2 := POWER(NO,3);
	DBMS_OUTPUT.PUT_LINE('The Square Of '||NO||' Is '||NO1);
	DBMS_OUTPUT.PUT_LINE('The Cube Of '||NO||' Is '||NO2);
END;
/
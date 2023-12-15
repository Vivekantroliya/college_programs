/* Write a program that accepts two values from the user then swap that value with eachother 
without using third variable. */

SET SERVEROUTPUT ON


DECLARE
	VALUE1 NUMBER(5);
	VALUE2 NUMBER(5);
BEGIN
	VALUE1 := &FIRST_VALUE ;
	VALUE2 := &SECOND_VALUE ;
	VALUE1 := VALUE1+VALUE2;
	VALUE2 := VALUE1-VALUE2;
	VALUE1 := VALUE1-VALUE2;
	
	DBMS_OUTPUT.PUT_LINE(VALUE1 ||' Is Replaced From Second Value To First Value.');
	DBMS_OUTPUT.PUT_LINE(VALUE2 ||' Is Replaced From First Value To Second Value.');
END;
/



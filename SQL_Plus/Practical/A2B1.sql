/* Write a program that accepts two values from the user then swap that value with eachother 
with using third variable. */

SET SERVEROUTPUT ON
SET FEEDBACK OFF
SET VERIFY OFF

DECLARE
	VALUE1 NUMBER(5);
	VALUE2 NUMBER(5);
	VALUE3 NUMBER(5);
BEGIN
	VALUE1 := &FIRST_VALUE ;
	VALUE2 := &SECOND_VALUE ;
	VALUE3 := VALUE1;
	VALUE1 := VALUE2;
	VALUE2 := VALUE3;

	DBMS_OUTPUT.PUT_LINE('FIRST VALUE IS ' ||VALUE1||'.');
	DBMS_OUTPUT.PUT_LINE('SECOND VALUE IS ' ||VALUE2||'.');
END;
/

SET SERVEROUTPUT OFF
SET FEEDBACK ON
SET VERIFY ON


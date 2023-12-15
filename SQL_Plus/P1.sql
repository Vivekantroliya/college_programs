/* Write a program to calculate the AREA of a circle and store that value in the table.
C_AREA (RADIUS NUMBER (5), AREA NUMBER (14,2)). */

SET SERVEROUTPUT ON
-- ACCEPT R1 PROMPT "Enter The Value For Radius : "

DECLARE
	PI CONSTANT NUMBER(7,2) := 3.14 ;
	R C_AREA.RADIUS%TYPE ;
	AREA C_AREA.RADIUS%TYPE ;
BEGIN
	R := &RADIUS ;
	AREA := PI*POWER(R,2);
	DBMS_OUTPUT.PUT_LINE('The Value Of PI : '||PI);
	DBMS_OUTPUT.PUT_LINE('The Value Of R  : '||R);
	DBMS_OUTPUT.PUT_LINE('The Area Of Circle Is '||AREA);

	INSERT INTO C_AREA VALUES(R,AREA);
END;
/

SELECT * FROM C_AREA;
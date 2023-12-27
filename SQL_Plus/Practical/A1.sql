/* Write a program to calculate the AREA of a circle and store that value in the table.
C_AREA (RADIUS NUMBER (5), AREA NUMBER (14,2)). */

SET SERVEROUTPUT ON
SET FEEDBACK OFF
SET VERIFY OFF

-- ACCEPT R1 PROMPT "Enter The Value For Radius : "

DECLARE
	PI CONSTANT NUMBER(3,2) := 3.14 ;
	R C_AREA.RADIUS%TYPE ;
	A C_AREA.AREA%TYPE ;
BEGIN
	R := &RADIUS ;
	A := PI*POWER(R,2);
	DBMS_OUTPUT.PUT_LINE('The Value Of PI : '||PI);
	DBMS_OUTPUT.PUT_LINE('The Value Of R  : '||R);
	DBMS_OUTPUT.PUT_LINE('The Area Of Circle Is '||A);
	INSERT INTO C_AREA VALUES(R,A);
END;
/

SELECT * FROM C_AREA;

SET SERVEROUTPUT OFF
SET FEEDBACK ON
SET VERIFY ON
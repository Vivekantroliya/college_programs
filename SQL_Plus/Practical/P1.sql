/*Write a PL/SQL block to find the maximum of 3 numbers.*/

SET SERVEROUTPUT ON
SET FEEDBACK OFF
SET VERIFY OFF

DECLARE

	A NUMBER(3);
	B NUMBER(3);
	C NUMBER(3);
	MX NUMBER(3);

BEGIN

	A := &A ;
	B := &B ;
	C := &C ;

	IF A>B AND A>C THEN
		MX := A ;
	ELSIF B>A AND B>C THEN
		MX := B ;
	ELSE 
		MX := C ;
	END IF;

	DBMS_OUTPUT.PUT_LINE('MAXIMUM NUMBER IS '||MX||' .');

END;
/

SET SERVEROUTPUT OFF
SET FEEDBACK ON
SET VERIFY ON

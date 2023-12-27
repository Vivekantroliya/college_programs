/*Write a function that returns the square of the given number. Execute this function using separate PL/SQL block and also without using PL/SQL block on command line.*/

SET SERVEROUTPUT ON
SET FEEDBACK OFF
SET VERIFY OFF

CREATE OR REPLACE FUNCTION SQUARE
(NO IN NUMBER)
RETURN NUMBER
AS
NO1 NUMBER;
BEGIN
	NO1 := NO*NO;
	RETURN NO1;
END;
/

SET SERVEROUTPUT OFF
SET FEEDBACK ON
SET VERIFY ON
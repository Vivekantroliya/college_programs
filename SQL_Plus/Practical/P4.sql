/*Write a procedure which takes temperature in Fahrenheit and show it in Celsius.*/

SET SERVEROUTPUT ON
SET FEEDBACK OFF
SET VERIFY OFF

CREATE OR REPLACE PROCEDURE TEMP_PRO
(F IN NUMBER,C OUT NUMBER)
AS
BEGIN
	C := (F-32)*5/9;
END;
/

SET SERVEROUTPUT OFF
SET FEEDBACK ON
SET VERIFY ON
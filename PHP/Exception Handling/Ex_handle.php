<?php
//create function with an exception

Function checkNum($number)
{
	if($number>5)
	{
		throw new Exception("Value Is Above Five.");
	}
//trigger exception in a "try" block
try
{
	checkNum(5);
	//If the exception is thrown,this next will not be shown
	echo "Value Is 5 Or Below.";
}
//catch exception
catch(Exception $e)
{
	echo $e->getMessage();
}
?>
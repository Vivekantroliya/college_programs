<?php
$link = mysqli_connect("localhost","root","","vivek");

//check connetion
if($link === false)
{
	die("ERROR:Could Not Connect.".mysqli_connect_error());
}

//Attempt Insert Query Execution
$sql = "INSERT INTO Persons VALUES(3,'MS','Dhoni','dhoni@gmail.com')";
if(mysqli_query($link,$sql))
{
	echo "Record Added Successfully...";
}
else
{
	echo "ERROR";
}

//Close Connection
mysqli_close($link);
?>
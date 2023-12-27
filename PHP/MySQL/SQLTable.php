<?php
$link = mysqli_connect("localhost","root","","vivek");

//check connetion
if($link === false)
{
	die("ERROR:Could Not Connect.".mysqli_connect_error());
}

//Attempt Create Table Query Execution
$sql = "CREATE TABLE Persons
		(persion_id INT(4) NOT NULL PRIMARY KEY AUTO_INCREMENT,
		First_Name CHAR(30) NOT NULL,
		Last_Name CHAR(30) NOT NULL,
		Email_Address VARCHAR(50))";

if(mysqli_query($link,$sql))
{
	echo "Table Created Successfully...";
}
else
{
	echo "ERROR: $sql.".mysqli_error($link);
}

//Close Connection
mysqli_close($link);
?>
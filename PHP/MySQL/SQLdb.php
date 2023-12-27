<?php
$link = mysqli_connect("localhost","root","");

//check connetion
if($link === false)
{
	die("ERROR:Could Not Connect.".mysqli_connect_error());
}

//Attempt Create Database Query Execution
$sql = "CREATE DATABASE vivek";
if(mysqli_query($link,$sql))
{
	echo "Database Successfully Created...";
}
else
{
	echo "ERROR: Could Not Able To Execute $sql.".mysqli_error($link);
}

//Close Connection
mysqli_close($link);
?>
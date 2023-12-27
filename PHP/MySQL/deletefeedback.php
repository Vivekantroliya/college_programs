<?php
$link = mysqli_connect("localhost","root","","vivek");
//Check Connetion
if($link === false)
{
	die("ERROR : Could Not Connect.".mysqli_connect_error());
}

//Attemp Insert Query Execution
$sql = "DELETE FROM feedback WHERE FIRSTNAME='VIRAT'";

if (mysqli_query($link,$sql))
{
	 echo "Records Deleted Successfully...";
}
else
{
	echo "ERROR : Could Not Able To Execute $sql.".mysqli_error($link);
}
//Close Connection
mysqli_close($link);
?>
<?php
$link = mysqli_connect("localhost","root","","vivek");
//Check Connetion
if($link === false)
{
	die("ERROR : Could Not Connect.".mysqli_connect_error());
}

//Mention "name" Attributes In Variable
$firstname = $_POST['firstname'];
$lastname  = $_POST['lastname'];
$dob	   = $_POST['dob'];
$email 	   = $_POST['email'];
$contactno = $_POST['contactno'];
$address   = $_POST['address'];
$comments  = $_POST['comments'];

//Attemp Insert Query Execution
$sql = "INSERT INTO feedback VALUES('$firstname','$lastname','$dob','$email','$contactno','$address','$comments')";

if (mysqli_query($link,$sql))
{
	 echo "Records Added Successfully...";
}
else
{
	echo "ERROR : Could Not Able To Execute $sql.".mysqli_error($link);
}
//Close Connection
mysqli_close($link);
?>
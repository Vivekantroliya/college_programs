<?php
$email = 'abc@yahoo.com';
//remove all illegal characters from email
$email = filter_var($email,FILTER_SANITIZE_EMAIL);
//validate email
if(!filter_var($email,FILTER_VALIDATE_EMAIL) === false)
{
	echo "$email is a valid email address.";
}
else
{
	echo "$email is not a valid email address.";
}
?>
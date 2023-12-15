<?php
class customException extends Exception
{
	public function errorMessage()
	{
		//error message
		echo "invalid email id format.";
	}
}
$email = "MCA1@marwadi.com";
try
{
	//check if
	if(filter_var($email,FILTER_VALIDATE_EMAIL)===FALSE)
	{
		//throw exception if email is not valid
		throw new customException($email);
	}
	//check for "marwadi" in mail address
	if(strpos($email,"marwadi")==TRUE)
	{
		throw new Exception("<b>$email</b> is marwadi email address.");
	}
	else
	{
		throw new Exception("<b>$email</b> is not marwadi email address.");
	}
}
catch(customException $e)
{
	echo $e->errorMessage();
}
catch(Exception $e)
{
	echo $e->getMessage();
}
?>
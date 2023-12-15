<?php
	session_start();
	if(isset($_SESSION['counter']))
	{
		$_SESSION['counter'] += 1;
	}
	else
	{
		$_SESSION['counter'] = 1;
	}
	$msg = "You have Visited this page ".$_SESSION['counter'];
	$msg .= " time in current session.";
?>

<html>
<head>
	<title>Setting up a php session</title>
</head>
<body>
<?php
	echo($msg);
?>
</body>
</html>
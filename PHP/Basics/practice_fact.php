<html>
<body>

<form method = "POST" action = "practice_fact.php">
 	ENTER NUMBER FOR FINDING FACTOTIAL : <input type="text" name="fact">
 	<center><input class="btn" type="submit" value='Submit'></center>
 </form>
<?php

	$n=($_POST);
	$a=1;
	for($i = 1;$i <= $n; $i++)
	{
		$a = $a * $i; 
	}

if(isset($_POST['num']) && array_key_exists('fact',$_POST))
{

	$a = $_POST[ 'fact' ];
	echo "<h4>The FActorial Of $a Is $n .</h4>";
}
?>

</body>
</html>
<?php
	setcookie("user1","MI");
	setcookie("user2","CSK");
	setcookie("user3","GT");
?>
<html>
<body>
<?php
	if(!isset($_COOKIE["user1"]))
	{
		echo "Sorry,Cookie is not found.";
	}
	else
	{
		echo "Mentioned Cookie is found.";
	}
?>
</body>
</html>
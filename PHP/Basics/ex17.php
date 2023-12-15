<?php
	$name1=array("Sonu","John","Vivek","Smith");
	$name2=array("Umesh","Sonu","Kartik","Smith");
	$name3=array_intersect($name1,$name2);
	foreach($name3 as $n)
	{
		echo"$n<br>";
	}
?>
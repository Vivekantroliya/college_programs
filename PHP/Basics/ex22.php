<?php

  $salaries=array("amar"=>20000,"akbar"=>10000,"anthony"=>5000);
	echo"salary of amar is:".$salaries['amar']."<br>";
	echo"salary of akbar is:".$salaries['akbar']."<br>";
	echo"salary of anthony is:".$salaries['anthony']."<br>";

  $salaries['amar']="high";
  $salaries['akbar']="medium";
  $salaries['anthony']="low";
  
	echo"salary of amar is:".$salaries['amar']."<br>";
	echo"salary of akbar is:".$salaries['akbar']."<br>";
	echo"salary of anthony is:".$salaries['anthony']."<br>";
  
?>
<?php

	echo"absolute function<br>";
	$abs1=abs(-4.2);
	$abs2=abs(5);
	$abs3=abs(-5);
	echo $abs1." ".$abs2." ".$abs3;
	
	echo"<br>";
	echo"ceiling function<br>";
	echo ceil(4.3)." ";
	echo ceil(9.9999)." ";
	echo ceil(-3.14);
	
	echo"<br>";
	echo"floor function<br>";
	echo floor(4.3)." ";
	echo floor(9.9999)." ";
	echo floor(-3.14);
	
	echo"<br>";
	echo"round function<br>";
	echo round(3.4);
	echo"<br>";
	echo round(3.5);
	echo"<br>";
	echo round(3.6);
	echo"<br>";
	echo round(3.66,0);
	echo"<br>";
	echo round(1.95583,2);
	echo"<br>";
	echo round(1241557,-3);
	echo"<br>";
	echo round(5.045,2);
	echo"<br>";
	echo round(5.055,2);
	echo"<br>";
	
	echo"<br>";
	echo"fmod function";
	$x=99;
	$y=5;
	$result = fmod($x,$y);
	echo"<br>";
	echo $result;
	
	echo"<br>";
	echo"power function";
	echo"<br>";
	var_dump(pow(2,8));
	
	echo"<br>";
	echo pow(2,8);
	
	echo"<br>";
	echo pow(0,0);
	
	echo"<br>";
	echo"square root function";
	echo"<br>";
	echo sqrt(9);
	echo"<br>";
	echo sqrt(10);
	
	echo"<br>";
	echo"<br>";
	echo"random function";
	echo"<br>";
	echo rand();
	echo"<br>";
	echo rand(100,999);
	echo"<br>";
	echo rand();
	
	echo"<br>";
	echo"<br>";
	echo"binary to decimal function";
	echo"<br>";
	echo bindec(1011);
	
	echo"<br>";
	echo"<br>";
	echo"decimal to binary function";	
	echo"<br>";
	echo decbin(11);
	
	echo"<br>";
	echo"<br>";
	echo"decimal to hexa-decimal function";	
	echo"<br>";
	echo dechex(52);
	
	echo"<br>";
	echo"<br>";
	echo"decimal octal function";	
	echo"<br>";
	echo decoct(1587);
	
	echo"<br>";
	echo"<br>";
	echo"hexa-decimal to decimal function";	
	echo"<br>";
	echo hexdec("ABC");
	
	echo"<br>";
	echo"<br>";
	echo"octal to decimal function";	
	echo"<br>";
	echo octdec(3063);
	
?>
	
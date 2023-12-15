<html>
<body>
	<?php
	//demo on continue
	$num=array(1,2,3,4,5);
	
	foreach ($num as $val){
		if($val==3)
		continue;
		echo"value is $val<br>";
	}
	?>
</body>
</html>
<html>
<body>

<?php
$marks=array(

	"Amar"=>array ("Physics"=>35,"Maths"=>30,"Chemistry"=>39),
	"Akbar"=>array("Physics"=>30,"Maths"=>32,"Chemistry"=>29),
	"Anthony"=>array ("Physics"=>31,"Maths"=>22,"Chemistry"=>39),
);

/* Accessing Multi-dimensional Array Values*/

	echo"Marks of Amar in Physics:";
	echo$marks['Amar']['Physics']."<br>";
	
	echo"Marks of Akbar in Maths:";
	echo$marks['Akbar']['Maths']."<br>";
	
	echo"Marks of Anthony in Chemistry:";
	echo$marks['Anthony']['Chemistry']."<br>";
	
?>

</body>
</html>
<pre>
<?php
echo max(1,3,5,6,7); 		//7
echo min(1,3,5,6,7);		//1

echo max(array(2,4,5));  	//5
echo min(array(2,4,5));  	//2

echo "<br>";

//with multiple arrays ,max compares from left to right
//so in our example : 2 == 2,but 4 < 5

$val1 = max(array(2,4,8),array(2,5,7));
$val2 = min(array(2,4,8),array(2,5,7));

//array(2,5,7)

print_r($val1);
print_r($val2);

//if both an array and non-array are given,the array is always returned as it's seen as the largest

$val3 = max('string',array(2,5,7),42);	//array(2,5,7)
$val4 = min('string',array(2,5,7),42);	//

print_r($val3);
print_r($val4);

?>
</pre>
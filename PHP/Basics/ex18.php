<pre>
<?php

$salary=array("Virat"=>"550000",
			  "Rohit"=>"250000",
			  "Dhavan"=>"200000");
print_r(array_change_key_case($salary,CASE_UPPER));

$salary=array("Virat"=>"550000",
			  "Rohit"=>"250000",
			  "Dhavan"=>"200000");
print_r(array_change_key_case($salary,CASE_LOWER));

$salary=array("Virat"=>"550000","Rohit"=>"250000","Dhavan"=>"200000","Surya"=>"200000","Hardik"=>"200000");
print_r(array_chunk($salary,2));

$season = array("summer","winter","monsoon");
echo "no of seasons are:".count($season);
?>
</pre>
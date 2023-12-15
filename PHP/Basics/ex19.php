<?php
//PHP Parameterized Function
function add($X,$Y)
{
$sum = $X+$Y;
echo "Sum=$sum<br><br>";
}
function sub($X,$Y)
{
$sub=$X-$Y;
echo "Diff=$sub<br><br>";
}
//call function,get two argument through input box and click on add or sub button
if(isset($_POST['add']))
{
	add($_POST['first'],$_POST['second']);
}
if(isset($_POST['sub']))
{
	sub($_POST['first'],$_POST['second']);
}
?>
<form method ="post">
Enter First Number:<input type="Number"name="first"/><br><br>
Enter Second Number:<input type="Number"name="second"/><br><br>
<input type="submit"name="add"value="ADDITION"/>
<input type="submit"name="sub"value="SUBTRACTION"/>
</form>

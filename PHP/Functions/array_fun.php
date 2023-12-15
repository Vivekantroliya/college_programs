<pre>
<?php
$info = array('Pizza','delicious','brownie');
//Listing All The Variables
list($a,$b,$c) = $info ;
echo "$a is $b and $c makes it special. \n";

echo "<br>";
//Listing Some Of Them 
list ($a, ,$c) =$info;
echo "$a with cold-drinks and $c. \n";

echo "<br>";
//Let's Keep Only The Third One
list( , ,$c) = $info;
echo "I need coffee with $c! \n";

echo "<br>";
$yes = array('this','is','an array');
echo is_array($yes)? 'array': 'not an array';

echo "<br>";
$no = 'this is a string';
echo is_array($no)? 'array': 'not an array';

echo "<br>";
$os = array('mac','nt','irix','linux');
if(in_array ('irix',$os))
        echo"got irix";
else
        echo"no match";

echo "<br>";
if(in_array ('mac',$os))
        echo"got mac";
else
        echo"no match";

echo "<br>";

$a = array('1.10',12.4,1.13);
if(in_array('12.4',$a,true))
        echo"'12.4'found with strict check. \n";
else
        echo"mis-match datatype.";

echo "<br>";
if(in_array(1.13,$a,true))
        echo"1.13 found with strict check. \n";
else
        echo"mis-match datatype.";

echo"<br>";
$transport = array('bike','car','bus','rail');
echo ($mode = current($transport));
echo"<br>";
echo ($mode = next($transport));
echo"<br>";
echo ($mode = next($transport));
echo"<br>";
echo ($mode = prev($transport));
echo"<br>";
echo ($mode = end($transport));
echo"<br>";

echo"<br>";
$array = array('step one','step two','step three','step four');
echo current($array)."<br/>\n";
next($array);
next($array);
echo current($array)."<br/>\n";
reset($array);
echo current($array)."<br/>\n";

echo"<br>";
echo"<h4>sort() function </h4>";
$fruit = array('lemon','orange','banana','apple');
sort($fruit);
foreach($fruit as $key => $val)
        echo"fruits[". $key ."]. $val . \n";

echo"<br>";
echo"<h4>rsort() function </h4>";
$fruits = array("d"=>'lemon',"a"=>'orange',"b"=>'banana',"c"=>'apple');
asort($fruits);
foreach($fruits as $key => $val)
        echo"$key = $val \n";

echo"<br>";
echo"<h4>arsort() function </h4>";
arsort($fruits);
foreach($fruits as $key => $val)
        echo"$key = $val \n";

echo"<br>";
echo"<h4>array_merge() function </h4>";
$array1 = array("color"=>'red',2,4);
print_r($array1);
$array2 = array("a","b","color"=>'green',"shape"=>'square',4);
print_r($array2);
$result = array_merge($array1,$array2);
print_r($result);
?>
</pre>
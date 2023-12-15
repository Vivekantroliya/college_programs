<pre>
<?php
$today = getdate();
print_r($today);

//return an associative array with information related to the timestamp.

echo "<br>";
$nextweek = time()+(7*24*60*60);

//7 days; 24 hours; 60 mins; 60 secs)

echo 'System date :'.date('Y-m-d')."\n";
echo 'next week 1 :'.date('d-m-Y',$nextweek)."\n";

//or using strtotime()

echo 'next week 2 :'.date('m-d-y',strtotime('+2week'))."\n";
echo "<br>";
echo date('d-m-y',mktime(9,0,0,8,15,2012));

//mktime(hour,minute,second,month,day,year)

echo "<br>";
echo date('l', mktime(2,3,4,8,15,1947));

?>
</pre>
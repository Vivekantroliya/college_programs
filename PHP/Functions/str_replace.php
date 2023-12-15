<?php
$vowels = array("a","e","i","o","u","A","E","I","O","U");
$onlyconsonants = str_replace ($vowels,"*","HELLO World of php...",$count);
echo $onlyconsonants;
echo $count;
echo "<br>";
$phrase = "you should eat fruits,vegtables and juice daily...";
$healthy = array("fruits","vegtables","juice");
$yummy = array("pizza","cold-drink","icecream");
$newphrase = str_replace($healthy,$yummy,$phrase,$count);
echo $newphrase;
echo $count;
echo "<br>";
$str1 = str_replace("ll","@","bollywood and hollywood...",$count);
echo $str1;
echo $count;  //2
?>
<?php

echo "<h4>chr function</h4>";
echo chr(65);
echo"<br>";
echo chr(97);

echo"<h4>ord function</h4>";
echo ord("M")."<br>";
echo ord("MEFGI");

echo"<h4>strtolower function</h4>";
echo strtolower("Welcome To MEFGI");

echo"<h4>strtoupper function</h4>";
echo strtoupper("WELCOME TO MEFGI");

echo"<h4>strlen function</h4>";
echo strlen("Welcome To MEFGI");

echo"<br>";

echo"<h4>sub string function</h4>";
$rest1 = substr("abcdef",-1);
echo $rest1;
echo"<br>";
$rest2 = substr("abcdef",-2);
echo $rest2;
echo"<br>";
$rest3 = substr("abcdef",-6,3);
echo $rest3;

echo"<br>";

echo"<h4>string comparison function</h4>";
echo strcmp("Hellow","Hellow");
echo"<br>";
echo strcmp("Hellow","hellow");

echo"<br>";

echo "<h4>string case comparison function</h4>";
$var1 = "Hellow";
$var2 = "Hellow";
if(strcasecmp($var1,$var2) == 0)
		echo'matching string';
else
		echo'mismatching string';

echo "<br>";

echo "<h4>string position function</h4>";
$newstring = 'abcdef abcdef';
$pos1=strpos($newstring,'a');
echo $pos1;
echo "<br>";
$pos2 = strpos ($newstring,'a',1);
echo $pos2;

echo"<br>";

echo "<h4>strstr function</h4>";
$email = 'name@example.com';
$domain = strstr ($email,'@');
echo $domain;
echo"<br>";
$user = strstr($email,'@',true);
echo $user;
echo"<br>";

echo"<h4>stristr (insensitive) function</h4>";
$email = 'USER@Example.com';
echo stristr($email,'e');
echo "<br>";
echo stristr($email,'e',true);
echo "<br>";

echo "<h4>string reverse function</h4>";
echo strrev("Hello");
echo "<br>";
echo strrev("This Spans Multiple Lines.The New Line Will Be Output As Well.");

?>
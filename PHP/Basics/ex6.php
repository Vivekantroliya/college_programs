<?php
echo"<h3>Post Increment<\h3><br>";
$a=5;
echo "Should be 5:".$a++."<br />\n";
echo "Should be 6:".$a."<br />\n";
echo "<h3>Pre Increment<\h3><br>";
//$a=5;
echo "Should be 6:".++$a."<br />\n";
echo "Should be 6:".$a."<br />\n";
echo"<h3>Post Decrement<\h3><br>";
//$a=5;
echo "Should be 5:".$a--."<br />\n";
echo "Should be 4:".$a."<br />\n";
echo"<h3>Pre Decrement<\h3><br>";
//$a=5;
echo "Should be 4:".--$a."<br />\n";
echo "Should be 4:".$a."<br />\n";
?>
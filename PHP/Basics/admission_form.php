<html>
<body>
	<style>
 		body 
 		{ 
 			color : #000080 ;
 			background-color : lightblue ;
 		}
 		.btn
 		{
 			background-color: yellow ;
 			border-radius: 50px;
 		}
 		.btn:hover{
 			background-color: black;
 			color: white;
 			transform: translate(10%);
 		}	
	</style>
	<form method='POST' action='admission_form.php'>
		<center><h2>Admission Form</h2></center>
		<table>
		<tr>
			<td>First Name </td>
			<td> <input type="text" name="fn"><br></td>
		</tr>
		<tr>
			<td>Middle Name </td>
			<td><input type="text" name="mn"><br></td>
		</tr>
		<tr>
			<td>Surname </td>
			<td><input type="text" name="sr"><br></td>
		</tr>
		<tr>
			<td>Birth Date </td>
			<td><input type="date" name="bd"><br></td>
		</tr>
		<tr>
			<td>Email </td>
			<td><input type="email" name="em"><br></td>
		</tr>
		<tr>
			<td>Gender </td>
			<td><input type="radio" name="gn" value="Male">Male<input type="radio" name="gn" value="Female">Female<br></td>
		</tr>
		<tr>
			<td>Course </td>		
			<td><select name="cu">
				<option></option>
				<option>MCA</option>
				<option>MBA</option>
				<option>M.Com.</option>
				<option>MA</option>
				<option>M.Sc.</option>
				<option>M.Tech.</option>
			</select><br></td>
		</tr>
		<tr>
			<td>City </td>
			<td><select name="ci">
				<option></option>
				<option>Ahmedabad</option>
				<option>Rajkot</option>
				<option>Morbi</option>
				<option>Wankaner</option>
				<option>Chotila</option>
				<option>Gondal</option>
				<option>Junagadh</option>
				<option>Keshod</option>
			</select><br></td>
		</tr>
		<tr>
			<td>Phone No. </td>
			<td><input type="text" name="pn"><br></td>
		</tr>
		<tr>
			<td>College Name </td>
			<td><input type="text" name="cn"><br></td>
		</tr>
		</table>
		<center><input class="btn" type="submit" value='Inquiry'></center>
	</form>
<?php
//retrive Name From Query String And Store To A Local Variable
if(isset($_POST) && array_key_exists('fn',$_POST) && array_key_exists('cu',$_POST) && array_key_exists('ci',$_POST) && array_key_exists('gn',$_POST))
{
	$a = $_POST[ 'fn' ];
	echo "<h4>First Name  : $a</h4>";
	$b = $_POST[ 'mn' ];
	echo "<h4>Middle Name : $b</h4>";
	$c = $_POST[ 'sr'];
	echo "<h4>Surname     : $c</h4>";
	$d = $_POST[ 'bd'];
	echo "<h4>Birth Date  : $d</h4>";
	$e = $_POST[ 'em'];
	echo "<h4>Email       : $e</h4>";
	$f = $_POST[ 'gn'];
	echo "<h4>Gender      : $f</h4>";
	$g = $_POST[ 'cu'];
	echo "<h4>Course      : $g</h4>";
	$h = $_POST[ 'ci'];
	echo "<h4>City        : $h</h4>";
	$i = $_POST[ 'pn'];
	echo "<h4>Phone No.   : $i</h4>";
	$j = $_POST[ 'cn'];
	echo "<h4>College Name: $j</h4>";


}
?>
</body>
</html>
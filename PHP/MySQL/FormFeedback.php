<html>
<head>
<title>
Registration Form
</title>
</head>
<body>
	<table border="1">
		<form action="insertfeedback.php" method="POST">
			<p>
				First Name :
				<input type="text" name="firstname" id="firstname">
			</p>
			<p>
				Last Name :
				<input type="text" name="lastname" id="lastname">
			</p>
			<p>
				Date Of Birth :
				<input type="date" name="dob" id="dob">
			</p>
			<p>
				Email Address :
				<input type="text" name="email" id="email">
			</p>
			<p>
				Contact No :
				<input type="text" name="contactno" id="contactno">
			</p>
			<p>
				Address :
				<input type="text" name="address" id="address">
			</p>
			<p>
				Comments :
				<input type="text" name="comments" id="comments">
			</p>
			<input type="submit" value="Submit">
		</form>
	</table>
</body>
</html>
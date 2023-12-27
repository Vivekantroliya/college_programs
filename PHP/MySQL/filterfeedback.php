<?php
$link = mysqli_connect("localhost","root","","vivek");
//Check Connetion
if($link === false)
{
	die("ERROR : Could Not Connect.".mysqli_connect_error());
}

//Attempt Select Query Execution
$sql = "SELECT FIRSTNAME,CONTACTNO,EMAIL,COMMENTS FROM feedback WHERE LASTNAME='DHONI'";
if($result = mysqli_query($link,$sql))
{
	if(mysqli_num_rows($result)>0)
	{
		echo"<table border=1>";
			echo"<tr>";
				echo"<th>First Name</th>";
				echo"<th>Contact No</th>";
				echo"<th>Email Address</th>";
				echo"<th>Comments</th>";
			echo"</tr>";
		while($row = mysqli_fetch_array($result))
		{
			echo"<tr>";
				echo"<td>".$row['FIRSTNAME']."</td>";
				echo"<td>".$row['CONTACTNO']."</td>";
				echo"<td>".$row['EMAIL']."</td>";
				echo"<td>".$row['COMMENTS']."</td>";
			echo"</tr>";
		}
		echo"</table>";
		//Close Result Set
		mysqli_free_result($result);
	}
	else
	{
		echo"No Record Matching Your Query Were Found.";
	}
}
else
{
	echo"ERROR : Could Not Able To Execute $sql.".mysqli_error($link);
}

//Close Connection
mysqli_close($link);
?>
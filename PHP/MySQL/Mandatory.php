<!-- TO CREATE A REGISTRATION FORM WITH MANDATORY VALIDATION. -->

<html>
   <head>
      <style>
         .error {color: #FF0000;}
      </style>
   </head>
   <body> 
      <?php
         // define variables and set to empty values
         $nameErr = $emailErr = $genderErr = $courseErr = "";
         $name = $email = $gender = $class = $course = $subject = "";
         
         if ($_SERVER["REQUEST_METHOD"] == "POST") 
			{
            if (empty($_POST["name"])) 
			   {
               $nameErr = "Name Is Required.";
            }
				else 
				{
               $name = test_input($_POST["name"]);
            }
            
            if (empty($_POST["email"]))
            {
               $emailErr = "Email Is Required.";
            }
            else
            {
               $email = test_input($_POST["email"]);      
               // check if e-mail address is well-formed
               if (!filter_var($email, FILTER_VALIDATE_EMAIL))
               {
                  $emailErr = "Invalid Email Format."; 
               }
            }
            
            if (empty($_POST["course"]))
            {
               $courseErr = "Course Is Required.";
            }
            else
            {
               $course = test_input($_POST["course"]);
            }
            
            if (empty($_POST["class"]))
            {
               $class = "";
            }
            else
            {
               $class = test_input($_POST["class"]);
            }
            
            if (empty($_POST["gender"]))
            {
               $genderErr = "Gender Is Required.";
            }
            else
            {
               $gender = test_input($_POST["gender"]);
            }
         }
         
         function test_input($data)
         {
            $data = trim($data);
            $data = stripslashes($data);
            $data = htmlspecialchars($data);
            return $data;
         }
      ?>
      <h2>Absolute Classes Registration</h2>      
      <p><span class = "error">* Required Fields.</span></p>      
      <form method = "POST" action = "<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
         <table>
            <tr>
               <td>Name:</td>
               <td><input type = "text" name = "name">
                  <span class = "error">* <?php echo $nameErr;?></span>
               </td>
            </tr>            
            <tr>
               <td>E-Mail: </td>
               <td><input type = "text" name = "email">
                  <span class = "error">* <?php echo $emailErr;?></span>
               </td>
            </tr>
            <tr>
               <td>Course:</td>
               <td><input type = "text" name = "course">
                  <span class = "error">* <?php echo $courseErr;?></span>
               </td>
            </tr>            
            <tr>
               <td>Classes:</td>
               <td> <textarea name = "class" rows = "5" cols = "40"></textarea></td>
            </tr>            
            <tr>
               <td>Gender:</td>
               <td>
                  <input type = "radio" name = "gender" value = "Female">Female
                  <input type = "radio" name = "gender" value = "Male">Male
                  <span class = "error">* <?php echo $genderErr;?></span>
               </td>
            </tr>
                     
            <tr>
               <td>Agree</td>
               <td><input type = "checkbox" name = "checked" value = "1"></td>
               <?php if(!isset($_POST['checked'])){ ?>
               <span class = "error">* <?php echo "You Must Agree To Terms.";?></span>
               <?php } ?> 
            </tr>            
            <tr>
               <td>
                  <input type = "submit" name = "submit" value = "Click Here"> 
               </td>
            </tr>
         </table>
      </form>
      <?php
         echo "<h2>Your Given Values Are As :</h2>";
         echo ("<p>Your Name Is $name</p>");
         echo ("<p>Your Email address is $email</p>");
         echo ("<p>Your Course Is $course</p>");
         echo ("<p>Your Class Info Is $class </p>");
         echo ("<p>Your Gender Is $gender</p>");
      ?>    
   </body>
</html>
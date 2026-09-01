<?php

$conn=mysqli_connect(
    "localhost",
    "root",
    "",
    "test"
);

$name=$_POST['name'];
$dob=$_POST['dob'];

$sql=
"INSERT INTO register(name,dob)
VALUES('$name','$dob')";

if(mysqli_query($conn,$sql))
    {
        echo "stored successfully";

    }
else
    {
        echo "Error";
    }
 ?>
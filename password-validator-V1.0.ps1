cls
$pass = $args[0]

# This is a condition that checks if the input of a user with ten characters or more
if($pass.Length -le 9){
    write-host -ForegroundColor red "- Short password, password length should be greater than or equal to 10 characters
** Be sure to follow this password policy (enter 10+ characters, use special characters, numbers and uppercase and lowercase letters).(1)"
}

# This is a condition that checks if user input meets our password policy
elseif ($pass -notmatch "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]"){
    write-host -ForegroundColor red "- Weak password, Be sure to follow this password policy:
(enter 10+ characters, use special characters, numbers and uppercase and lowercase letters).(1)"
}

 
else {
    write-host -ForegroundColor green " - Succeeded, The password is very strong(0)"
}

def checkPasswordStrength(password):
    length = len(password)
    containsUpper = any(char.isupper() for char in password)
    containsLower = any(char.islower() for char in password)
    containsDigit = any(char.isdigit() for char in password)
    conatinsSpecialChar = any(char in '!@#$%^&*()_+-=<>?,./;\'\\][}{|' for char in password)
    
    if length>=8 and conatinsSpecialChar and containsDigit and containsLower and containsUpper:
        return 'Strong Password'
    elif length>=8 and (containsUpper or containsLower) and containsDigit:
        return "Moderate Password"
    else:
        return  "Weak Password"
    
x = True
while(x):
    password = input("Enter a password to check its strength: ")
    result = checkPasswordStrength(password)
    print("The password strength is : ", result)
    x = input("Enter 1 to continue or 0 for quit: ")
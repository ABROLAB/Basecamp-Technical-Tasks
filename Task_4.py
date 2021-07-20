'''
Create a password validator function that takes in the 
password as its argument and returns an integer value 
you can evaluate to determine the password strength. 
Using the following validators:
0 -> very weak e.g. a password with only strings
1 -> weak e.g. a password with only numbers
2 -> strong e.g. a password containing strings and numbers
3 -> very strong e.g. a password containing strings, numbers 
and special characters (!,@,#,$,%, etc)
'''
def Password_Validator():
    import re
    password = input('Enter the password to validate: ')
    response = False
    strength = 0
    
    if password.isalpha() == True:
        response = True
        strength = 0
    elif (password.isnumeric() == True):
        response = True
        strength = 1
    elif password.isalnum() == True:
        response = True
        strength = 2
    elif (re.search("\s", password) == False) and password.isalnum() == False:
        strength = 3
    else:
        response = False
    
    if response == True:
        return strength
    
Result = Password_Validator()
print(Result)

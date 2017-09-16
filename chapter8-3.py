def is_password_valid(password):
    if(has_number(password) and has_uppercase(password) and has_lowercase(password)  
       and password.isalnum() and len(password)>7):
        print("Password is Accepted")
    else:
        print("■ A password must have at least eight characters.")
        print("■ A password must consist of only letters and digits.")
        print("■ A password must contain at least two digits.")
        
def has_number(s1):
    return any(char.isdigit() for char in s1)

def has_uppercase(s1):
    return any(char.isupper() for char in s1)

def has_lowercase(s1):
    return any((not char.isupper() and char.isalpha()) for char in s1)



password=input("Enter password :")
is_password_valid(password)

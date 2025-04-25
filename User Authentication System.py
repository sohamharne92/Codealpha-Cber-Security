import hashlib


stored_password_hash = "5f4dcc3b5aa765d61d8327deb882cf99"  

def authenticate_user(username, password):
    
    password_hash = hashlib.md5(password.encode()).hexdigest()
    
    if password_hash == stored_password_hash:
        print("Authentication Successful")
    else:
        print("Authentication Failed")



username_input = input("Enter username: ")
password_input = input("Enter password: ")

authenticate_user(username_input, password_input)

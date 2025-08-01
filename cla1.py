import sys

def login():
    
    username = "Muzammil99"
    password = sys.argv[1]

    if len(password) == 10:
      print("Login Successful!")
    else:
      print("password not matched")
login()
from user import user
from hashUtil import hashData
from usersUtil import getAllUsernames, saveDataInUsers

def signup():

    usernameList = getAllUsernames()

    while True:
        username = input("Enter New Username: ")
        if not len(username) > 0:
            print("Username can't be blank")
            continue
        if username in usernameList:
            print("This username is already taken")
            return None
        else:
            break
    while True:
        password = input("Enter New Password: ")
        if not len(password) > 0:
            print("Password can't be blank")
            continue
        else:
            break
    
    saveDataInUsers(username, password)
    print("Creating account...")
    print("Account has been created")

    return username
    
from usersUtil import getAllUsers
from hashUtil import hashData, verifyData
from user import user

def login():

    userDataList = getAllUsers()
    while True:
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        loginSuccess = False
        for userData in userDataList:
            if username == userData.username:
                if verifyData(userData.password, password):
                    loginSuccess = True
                    break

        if loginSuccess:
            break
        else:
            print("Wrong Credentials")
            return None

    return username
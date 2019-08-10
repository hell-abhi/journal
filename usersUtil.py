import os
from user import user
from hashUtil import hashData

def getAllUsers():

    userDataList = []
    with open('users/users.txt', 'r') as f:
        for line in f:
            current = line.split(' ')
            currentUser = user(current[0], current[1])
            userDataList.append(currentUser)

    return userDataList

def getAllUsernames():

    userDataList = getAllUsers()
    usernameList = []
    
    for userData in userDataList:
        usernameList.append(userData.username)

    return usernameList

def saveDataInUsers(username, password):

    with open("users/users.txt", "a") as f:
        if os.path.getsize("users/users.txt") > 0:
            f.write("\n")
        f.write(username + " " + hashData(password))
import sys
from login import login
from signup import signup
from createJournal import createJournal
from listJournal import listJournal

while True:
    loginSignup = int(input("Enter 1 for Signup or 2 for Login or 3 for exit\n"))

    if loginSignup == 1:
        username = signup()
        if username is None:
            continue
        break
    elif loginSignup == 2:
        username = login()
        if username is None:
            continue
        break
    elif loginSignup == 3:
        sys.exit()
    else:
        print("Please choose correct option")
        continue

while True:
    journalOption = int(input("Enter 1 to list all your entries or 2 to create a new entry or 3 for exit\n"))
    if journalOption == 1:
        listJournal(username)
        continue
    elif journalOption == 2:
        createJournal(username)
        continue
    elif journalOption == 3:
        sys.exit()
    else:
        print("Please choose correct option")
        continue

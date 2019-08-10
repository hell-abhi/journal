from encryptionUtil import readKey
from journalsUtil import getJournal
from datetime import datetime
from encryptionUtil import readKey
from cryptography.fernet import Fernet

def listJournal(username):

    journalDataList = getJournal(username)
    key = readKey()
    fernetKey = Fernet(key)
    print("Your Journal Entries: ")
    print("****************************************************")
    for journalData in journalDataList:
        print(datetime.utcfromtimestamp(int(float(journalData.timestamp.rstrip()))).strftime('%d %b %Y %I:%M%p'), end = ' ')
        decryptedText = str(fernetKey.decrypt(bytes(journalData.entry[2:-1], 'utf-8')))[2:-1]
        print(decryptedText)

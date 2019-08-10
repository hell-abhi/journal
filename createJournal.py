import time
from cryptography.fernet import Fernet
from journalsUtil import getJournal, overwriteJournalEntry, saveJournalEntry
from journal import journal
from encryptionUtil import readKey

def createJournal(username):

    key = readKey()
    fernetKey = Fernet(key)
    text = input("Write your new entry: ")
    encodeText = text.encode('utf-8')
    encryptedText = fernetKey.encrypt(encodeText)
    currentTime = time.time()
    journalDataList = getJournal(username)
    journalEntry = journal(currentTime, encryptedText, username)
    if len(journalDataList) == 3:
        journalDataList.pop(0)
        journalDataList.append(journalEntry)
        overwriteJournalEntry(journalDataList)
    else:
        saveJournalEntry(journalEntry)
    print("Saved your entry in the journal")

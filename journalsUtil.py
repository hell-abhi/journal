from pathlib import Path
from journal import journal

def createJournalFileIfNotExists(username):

    journalFile = Path("journals/" + username + ".txt")
    if not journalFile.is_file():
        file = open("journals/" + username + ".txt", "w")
        file.close()
    
def getJournal(username):

    createJournalFileIfNotExists(username)
    journalDataList = []
    with open('journals/' + username + ".txt", 'r') as f:
        while True:
            timestamp = f.readline().rstrip()
            entry = f.readline().rstrip()
            if not entry:
                break
            currentEntry = journal(timestamp, entry, username)
            journalDataList.append(currentEntry)

    return journalDataList

def saveJournalEntry(journal):

    createJournalFileIfNotExists(journal.username)
    with open('journals/' + journal.username + ".txt", "a") as f:
        f.write(str(journal.timestamp) + "\n")
        f.write(str(journal.entry) + "\n")

def overwriteJournalEntry(journalList):

    with open('journals/' + journalList[0].username + ".txt", "w+") as f:
        for journalEntry in journalList:
            f.write(str(journalEntry.timestamp) + "\n")
            f.write(str(journalEntry.entry) + "\n")
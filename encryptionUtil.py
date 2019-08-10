from cryptography.fernet import Fernet

def generateKey():
    key = Fernet.generate_key()
    file = open('data/key.key', 'wb')
    file.write(key)
    file.close()

def readKey():
    file = open('data/key.key', 'rb')
    key = file.read()
    file.close()
    return key

# generateKey()
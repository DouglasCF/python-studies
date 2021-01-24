from cryptography.fernet import Fernet

key = b'ntLaRE-8-a81Bqa74aCL6ejFW4hr6ZO9m0fWbDOmys8='
message = input('Enter a message: ')

f = Fernet(key)
encrypted = f.encrypt(message.encode())
print(encrypted.decode("utf-8"))

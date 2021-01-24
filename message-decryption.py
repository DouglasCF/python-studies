from cryptography.fernet import Fernet

key = b'ntLaRE-8-a81Bqa74aCL6ejFW4hr6ZO9m0fWbDOmys8='
message = bytes(input('Enter a encrypted message: '), encoding='utf8')

f = Fernet(key)
decrypted = f.decrypt(message)
print(decrypted.decode("utf-8"))

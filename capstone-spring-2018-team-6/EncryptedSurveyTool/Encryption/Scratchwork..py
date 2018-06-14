import pyaes

# A 256 bit (32 byte) key

key = "32bit32bit32bit32bit32bit32bit!!"
plaintext = "Sore wa kanojo ga itta kotodearu"

print ("This is the plaintext: " + plaintext)

# key must be bytes, so we convert it
key = key.encode( 'utf-8')

aes = pyaes.AESModeOfOperationCTR(key)
ciphertext = aes.encrypt(plaintext)

# show the encrypted data
print ("This is the encrypted text")
print ( ciphertext)

# DECRYPTION
# CRT mode decryption requires a new instance be created
aes = pyaes.AESModeOfOperationCTR(key)

# decrypted data is always binary, need to decode to plaintext
decrypted = aes.decrypt(ciphertext).decode('utf-8')

print ("This is now the decrypted text: " + decrypted)

# True
print("Is the string the same as it started?:")
print (decrypted == plaintext)
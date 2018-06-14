import pyaes

print("Welcome to the Encryption Wizard!")

print("We will get started encrypting a string and outputting the string to a file.")

key = input("Enter your key for the 256-bit encryption: ")
append = "0" # The key will be padded with zeros as a proof of concept.  AES-256 requires a 256bit key, or 32 bytes.
print ("The length of the key is: " + str(len(key)))
while (len(key) < 32):  #This will add zeroes to the key.  This is known as padding the key.
    key += append

while (len(key) > 32):  #This will force the system to re-check the key, as it cannot be greater than 32 bytes.
    key = input("Key must be less than 256-bit (32 bytes).  Please try again: ")
    while (len(key) < 32):
        key += append
print ("This is the key you will use: " + key)


#Now it's time to implement what is to be encrypted.

plaintext = input("What is the string you wish to encrypt?:  ")

# key must be bytes, so we convert it
key = key.encode( 'utf-8')

aes = pyaes.AESModeOfOperationCTR(key) #Setting up an instance of PyAES...

ciphertext = aes.encrypt(plaintext)  #Actually encrypting the string...

# show the encrypted data
print ("This is the encrypted text")
print (ciphertext)




# DECRYPTION
# CRT mode decryption requires a new instance be created
aes = pyaes.AESModeOfOperationCTR(key)

# decrypted data is always binary, need to decode to plaintext
decrypted = aes.decrypt(ciphertext).decode('utf-8')

print ("This is now the decrypted text: " + decrypted)

# True
print("Is the string the same as it started?:")
print (decrypted == plaintext)


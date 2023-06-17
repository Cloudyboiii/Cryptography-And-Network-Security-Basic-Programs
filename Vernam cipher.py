# import random

# def vernam_cipher(plaintext, key):
#     ciphertext = ""
#     for i in range(len(plaintext)):
#         char = ord(plaintext[i]) ^ ord(key[i])
#         ciphertext += chr(char)
#     return ciphertext

# plaintext = input("Enter plaintext: ")
# key = input("Enter key: ")

# # Make sure the key is at least as long as the plaintext
# if len(key) < len(plaintext):
#     print("Error: key must be at least as long as the plaintext")
# else:
#     # Generate a random key if none was provided
#     if key == "":
#         key = "".join([chr(random.randint(0, 255)) for i in range(len(plaintext))])

#     ciphertext = vernam_cipher(plaintext, key)
#     print("Ciphertext:", ciphertext)


# def vernam_encrypt(plaintext, key):
#     ciphertext = ""
#     for i in range(len(plaintext)):
#         char = chr((ord(plaintext[i]) + ord(key[i])) % 128)
#         ciphertext += char
#     return ciphertext

# # Prompt the user for the plaintext and the key
# plaintext = input("Enter the plaintext: ")
# key = input("Enter the key: ")

# # Ensure that key is at least as long as plaintext
# while len(key) < len(plaintext):
#     key += key

# # Encrypt the plaintext
# ciphertext = vernam_encrypt(plaintext, key)
# print("Ciphertext: " + ciphertext)


# def vernam(plain_text,key):

#     # convert into lower cases and remove spaces
    
#     plain_text=plain_text.replace(" ","")
#     key=key.replace(" ","")
#     plain_text=plain_text.lower()
#     key=key.lower()
    
#     # conditional statements
#     if(len(plain_text)!=len(key)):
#         print("Lengths are different")
        
#     else:
#         cipher_text=""
        
#         # iterating through the length
#         for i in range(len(plain_text)):
#             k1=ord(plain_text[i])-97
#             k2=ord(key[i])-97
#             s=chr((k1+k2)%26+97)
#             cipher_text+=s
#         print("Enrypted message is: ",cipher_text)


# plain_text=input("Enter the message: ")
# key=input("Enter the one time pad: ")
# vernam(plain_text,key)


# def vernam(plaintext, key):

errorMessage = "Error: Length of Key Must be >= Length of Plaintext"
mappingsDict = {}

def main():

    print()
    # Taking inputs from the user
    plaintext = input("Enter the plaintext : ")
    key = input("Enter the key (length should be >= length of plaintext) : ")
    print()

    # Initializing alphabets for rotating
    alphabets = "abcdefghijklmnopqrstuvwxyz".upper()
    # Initializing values to alphabets
    for alphabet in alphabets:
        mappingsDict[alphabet] = ord(alphabet) - 65

    plaintext = plaintext.upper()
    key = key.upper()

    # Checking if key is invalid
    if len(key) < len(plaintext):
        print(errorMessage)
    # Else applying algorithm
    else:
        # Encryption
        ciphertext = vernamEncryption(plaintext, key)

        # Printing answers
        print()
        print("Encrypted ciphertext is : ", ciphertext)
        print("Decrypted plaintext is  : ", plaintext)
        print()
    return

def vernamEncryption(plaintext, key):
    """Function to encrypt the plaintext using Vernam Encryption."""

    # Initializing ciphertext
    ciphertext = ''

    for i in range(len(plaintext)):
        ptLetter = plaintext[i]
        keyLetter = key[i]
        # Performing vernam encryption step
        sum = mappingsDict[ptLetter] + mappingsDict[keyLetter]
        # Subtracting 26 if sum overflows above values
        if sum >= 26:
            sum -= 26
        # Adding to ciphertext
        ciphertext += chr(sum + 65)

    # Returning ciphertext
    return ciphertext

if __name__ == "__main__":
    main()
    
# import numpy as np

# def hill_cipher_encrypt():
#     # Get the key matrix from user input
#     key = np.array([[int(x) for x in input("Enter the 4 values of key matrix (separated by space): ").split()]])
#     key = key.reshape(2,2)
#     # Get the plaintext from user input
#     plaintext = input("Enter the plaintext: ")
#     # Remove spaces from plaintext and convert to uppercase
#     plaintext = plaintext.replace(" ", "")
#     plaintext = plaintext.upper()
#     # Pad plaintext with 'X' if its length is odd
#     if len(plaintext) % 2 != 0:
#         plaintext += "X"
#     # Divide plaintext into blocks of 2 characters
#     blocks = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
#     # Initialize the ciphertext as an empty string
#     ciphertext = ""
#     # Encrypt each block of plaintext
#     for block in blocks:
#         # Convert each block to a vector of numbers
#         block = np.array([ord(block[0]) - ord('A'), ord(block[1]) - ord('A')])
#         # Multiply the key matrix with the block vector
#         result = np.dot(key, block) % 26
#         # Convert the numbers back to characters and append to the ciphertext
#         result = [chr(i + ord('A')) for i in result]
#         ciphertext += "".join(result)
#     return ciphertext

# def hill_cipher_decrypt(ciphertext,key):
#     # Find the inverse of the key matrix
#     key_inverse = np.linalg.inv(key)
#     # Divide ciphertext into blocks of 2 characters
#     blocks = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
#     # Initialize the plaintext as an empty string
#     plaintext = ""
#     # Decrypt each block of ciphertext
#     for block in blocks:
#         # Convert each block to a vector of numbers
#         block = np.array([ord(block[0]) - ord('A'), ord(block[1]) - ord('A')])
#         # Multiply the key_inverse matrix with the block vector
#         result = np.dot(key_inverse, block) % 26
#         # Convert the numbers back to characters and append to the plaintext
#         result = [chr(i + ord('A')) for i in result]
#         plaintext += "".join(result)
#     return plaintext

# # Example usage
# ciphertext = hill_cipher_encrypt()
# print("Ciphertext: ",ciphertext)
# plaintext=hill_cipher_decrypt(ciphertext,key)
# print("Plaintext: ",plaintext)


# import numpy as np

# def encrypt(plaintext, key):
#     # Convert key and plaintext to numerical form
#     key_matrix = np.array([[ord(c) - ord('A') for c in row] for row in key])
#     plaintext_vector = np.array([ord(c) - ord('A') for c in plaintext])
    
#     # Encrypt the plaintext using the key matrix
#     ciphertext_vector = np.matmul(key_matrix, plaintext_vector) % 26
    
#     # Convert the ciphertext vector back to letters
#     ciphertext = ''.join([chr(c + ord('A')) for c in ciphertext_vector])
#     return ciphertext

# # key = input("Enter Key - ")
# # plaintext = input("Enter PT - ")
# # ciphertext = encrypt(plaintext, key)
# # print("Ciphertext: ", ciphertext)
# key = "HILL"
# plaintext = "EXAM"
# ciphertext = encrypt(plaintext, key)
# print("Ciphertext: ", ciphertext)




# def decrypt(ciphertext, key):
#     # Convert key and ciphertext to numerical form
#     key_matrix = np.array([[ord(c) - ord('A') for c in row] for row in key])
#     ciphertext_vector = np.array([ord(c) - ord('A') for c in ciphertext])

#     # Find the inverse of the key matrix
#     key_matrix_inv = np.linalg.inv(key_matrix)
    
#     # Decrypt the ciphertext using the inverse key matrix
#     plaintext_vector = np.matmul(key_matrix_inv, ciphertext_vector) % 26
    
#     # Convert the plaintext vector back to letters
#     plaintext = ''.join([chr(c + ord('A')) for c in plaintext_vector])
#     return plaintext

# # key = "HILL"
# # ciphertext = "EXAM"
# plaintext = decrypt(ciphertext, key)
# print("Plaintext: ", plaintext)



# import numpy as np

# def encrypt(plaintext, key):
#     key_matrix = key_gen(key)
#     plaintext_vector = np.array([ord(c) - ord('A') for c in plaintext])
#     ciphertext_vector = (np.matmul(key_matrix, plaintext_vector) % 26)
#     return ''.join([chr(c + ord('A')) for c in ciphertext_vector])

# def decrypt(ciphertext, key):
#     key_matrix = key_gen(key)
#     key_matrix_inv = np.linalg.inv(key_matrix)
#     ciphertext_vector = np.array([ord(c) - ord('A') for c in ciphertext])
#     plaintext_vector = (np.matmul(key_matrix_inv, ciphertext_vector) % 26)
#     return ''.join([chr(c + ord('A')) for c in plaintext_vector])

# def key_gen(key):
#     key = key.upper()
#     key_matrix = np.zeros((len(key), len(key)))
#     for i in range(len(key)):
#         key_matrix[i,i] = ord(key[i]) - ord('A')
#     return key_matrix

# key = input("Enter Key - ")
# plaintext = input("Enter PT - ")
# # key = "abcdef"
# # plaintext = "HELLOWORLD"
# ciphertext = encrypt(plaintext, key)
# print("Ciphertext: ", ciphertext)
# plaintext = decrypt(ciphertext, key)
# print("Plaintext: ", plaintext)


import numpy as np

def multiplication(keyMatrix, plainText):
    plainTextMatrix = list([ord(i) - 65] for i in plainText)
    result = np.zeros([len(plainTextMatrix), 1], dtype = int)
    result = np.dot(keyMatrix, plainTextMatrix)
    return result

def encrypt(message, keyMatrix, n):
    cipherText = ""
    for i in range(0, len(message), n):
        resultMatrix = multiplication(keyMatrix, message[i : i + n])
    for i in range(n):
      cipherText += chr(resultMatrix[i][0] % 26 + 65)
    return cipherText

keyMatrix = [[17, 17, 5], [21, 18, 21], [2, 2, 19]]

n = len(keyMatrix)
message = input("enter message: ")
print("Message :", message)
print("Key Matrix :", keyMatrix)
if len(message)%n != 0:
    for i in range(n - len(message) % n):
        message += 'X'
cipherText = encrypt(message, keyMatrix, n)
print("Cipher Text :", cipherText)


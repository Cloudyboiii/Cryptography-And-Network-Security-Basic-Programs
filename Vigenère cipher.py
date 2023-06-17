# def encode(plaintext, key):
#     key_len = len(key)
#     key_as_int = [ord(i) for i in key]
#     plaintext_int = [ord(i) for i in plaintext]
#     ciphertext = ''
#     for i in range(len(plaintext_int)):
#         x = (plaintext_int[i] + key_as_int[i % key_len]) % 26
#         x += ord('A')
#         ciphertext += chr(x)
#     return ciphertext

# def decode(ciphertext, key):
#     key_len = len(key)
#     key_as_int = [ord(i) for i in key]
#     ciphertext_int = [ord(i) for i in ciphertext]
#     plaintext = ''
#     for i in range(len(ciphertext_int)):
#         x = (ciphertext_int[i] - key_as_int[i % key_len] + 26) % 26
#         x += ord('A')
#         plaintext += chr(x)
#     return plaintext

# plaintext = input('Enter string - ')
# key = input('Enter key in string - ')
# # plaintext = "ATTACKATDAWN"
# # key = "SECRET"

# ciphertext = encode(plaintext, key)
# print("Encoded message: ", ciphertext)

# decoded_message = decode(ciphertext, key)
# print("Decoded message: ", decoded_message)


def encode(plaintext, key):
    key_len = len(key)
    key_as_int = [ord(i) % 32 for i in key]
    plaintext_int = [ord(i) % 32 for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        x = (plaintext_int[i] + key_as_int[i % key_len]) % 26
        x += ord('A') if plaintext[i].isupper() else ord('a')
        ciphertext += chr(x)
    return ciphertext

def decode(ciphertext, key):
    key_len = len(key)
    key_as_int = [ord(i) % 32 for i in key]
    ciphertext_int = [ord(i) % 32 for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        x = (ciphertext_int[i] - key_as_int[i % key_len] + 26) % 26
        x += ord('A') if ciphertext[i].isupper() else ord('a')
        plaintext += chr(x)
    return plaintext

plaintext = input('Enter string - ')
key = input('Enter key in string - ')

ciphertext = encode(plaintext, key)
print("Encoded message: ", ciphertext)

decoded_message = decode(ciphertext, key)
print("Decoded message: ", decoded_message)

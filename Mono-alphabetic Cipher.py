# def encrypt(plaintext, key):
#     ciphertext = ""
#     for char in plaintext:
#         if char.isalpha():
#             shift = ord(key[ord(char) % len(key)]) % 26
#             char = chr((ord(char) + shift - 97) % 26 + 97)
#         ciphertext += char
#     return ciphertext

# def decrypt(ciphertext, key):
#     plaintext = ""
#     for char in ciphertext:
#         if char.isalpha():
#             shift = ord(key[ord(char) % len(key)]) % 26
#             char = chr((ord(char) - shift - 97) % 26 + 97)
#         plaintext += char
#     return plaintext

# key = "secretkey"
# plaintext = "secret message"
# ciphertext = encrypt(plaintext, key)
# print("Ciphertext:", ciphertext)
# print("Plaintext:", decrypt(ciphertext, key))

# keys = {
#    'a': 'm',
#    'b': 'n',
#    'c': 'b',
#    'd': 'v',
#    'e': 'c',
#    'f': 'x',
#    'g': 'z',
#    'h': 'a',
#    'i': 's',
#    'j': 'd',
#    'k': 'f',
#    'l': 'g',
#    'm': 'h',
#    'n': 'j',
#    'o': 'k',
#    'p': 'l',
#    'q': 'p',
#    'r': 'o',
#    's': 'i',
#    't': 'u',
#    'u': 'y',
#    'v': 't',
#    'w': 'r',
#    'x': 'e',
#    'y': 'w',
#    'z': 'q',
# 	' ': ' ',
# }

# reverse_keys={}
# for key,value in keys.items():
#     reverse_keys[value]=key


# def encrypt(text):
#     text=str(text)
#     encrypting=[]
#     for l in text:
#         encrypting.append(keys.get(l,l))
#     print(''.join(encrypting))

# def decipher(text):
#     text=str(text)
#     decrypted=[]
#     for l in text:
#         decrypted.append(reverse_keys.get(l,l))
#     print(''.join(decrypted))

# x = input("Enter text")


# print(encrypt(x))
# y = encrypt(x)


# print(decipher(y))


# print(encrypt("hej"))
# print(decipher("acd"))



# def encrypt(plaintext, key):
#     ciphertext = ""
#     for char in plaintext:
#         if char.isalpha():
#             shift = ord(key[ord(char) - ord('a')]) - ord('a')
#             ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
#         else:
#             ciphertext += char
#     return ciphertext

# def decrypt(ciphertext, key):
#     plaintext = ""
#     for char in ciphertext:
#         if char.isalpha():
#             shift = ord(key[ord(char) - ord('a')]) - ord('a')
#             plaintext += chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
#         else:
#             plaintext += char
#     return plaintext

# key = "qwertyuiopasdfghjklzxcvbnm"
# plaintext = "hello world"
# ciphertext = encrypt(plaintext, key)
# print(ciphertext)
# decrypted_text = decrypt(ciphertext, key)
# print(decrypted_text)


mac={'a':'m','b':'n','c':'b','d':'v','e':'c','f':'x','g':'z','h':'a','i':'s','j':'d','k':'f','l':'g','m':'h','n':'j','o':'k','p':'l','q':'p','r':'o','s':'i','t':'u','u':'y','v':'t','w':'r','x':'e','y':'w','z':'q','':'',
'A':'M','B':'N','C':'B','D':'V','E':'C','F':'X','G':'Z','H':'A','I':'S','J':'D','K':'F','L':'G','M':'H','N':'J','O':'K','P':'L','Q':'p','R':'O','S':'I','T':'U','U':'Y','V':'T','W':'R','X':'E','Y':'W','Z':'Q'}

enc = ""
dec = ""
a = input('Enter string - ')

# ENCRYPTION
for i in a:
    temp = i
    for x in mac.keys():
        if(temp == x):
            enc += mac[temp]

# DECRYPTION
for i2 in enc:
    temp2 = i2
    for x,y in mac.items():
        if(y == temp2):
            dec += x

print("Encoded code is - " + enc + "\n")
print("Decoded text of " + enc + " is " + dec)


# key = {'a':'m','b':'n','c':'b','d':'v','e':'c','f':'x','g':'z','h':'a','i':'s','j':'d','k':'f','l':'g','m':'h','n':'j','o':'k','p':'l','q':'p','r':'o','s':'i','t':'u','u':'y','v':'t','w':'r','x':'e','y':'w','z':'q','':'',
# 'A':'M','B':'N','C':'B','D':'V','E':'C','F':'X','G':'Z','H':'A','I':'S','J':'D','K':'F','L':'G','M':'H','N':'J','O':'K','P':'L','Q':'p','R':'O','S':'I','T':'U','U':'Y','V':'T','W':'R','X':'E','Y':'W','Z':'Q'}

# enc = ""
# dec = ""

# x = input("Enter The String")


# def Encrypt(x):
#     for i in x:
#         cloudy = i
#         for y in key.keys():
#             if(cloudy == y):
#                 enc += key[cloudy]

# def Decrypt(x):
#     for i in enc:
#         cloudy = i
#         for x,y in key.items():
#             if y == cloudy:
#                 decrypt += x


# print("Encoded code is - " + enc + "\n")
# print("Decoded text of " + enc + " is " + dec)

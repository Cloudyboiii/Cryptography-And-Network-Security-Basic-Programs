def encrypt(text,s):
	result = ""
	for i in range(len(text)):
		char = text[i]
		if (char.isupper()):
			result += chr((ord(char) + s - 65) % 26 + 65)
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)
	return result

text = input("Enter text : ")
s = int(input("Enter key : "))
print ("Text : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(text,s))

z = encrypt(text,s).strip()

def decrypt():

    letters = 'abcdefghijklmnopqrstuvwxyz'
    letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    decrypted_text =""

    for ch in z:
        if ch in letters:
            position = letters.find(ch)
            new_pos = (position - s) % 26
            new_char = letters[new_pos]
            decrypted_text += new_char

        elif ch in letter:
            position = letter.find(ch)
            new_pos = (position - s) % 26
            new_char = letter[new_pos]
            decrypted_text += new_char

        else:
            decrypted_text += ch

    print("Your decrypted message is: " , decrypted_text)
    # print(decrypted_text)

decrypt()


# def decrypt(y,s):
# 	result = ""
# 	for i in range(len(text)):
# 		char = text[i]
# 		if (char.isupper()):
# 			result += chr((ord(char) - s-65) % 26 + 65)
# 		else:
# 			result += chr((ord(char) - s - 97) % 26 + 97)
# 	return result

# z = decrypt(y,s)
# print(z)



# PT = print(input("Enter Plain text"))
# key = print(int(input("Enter the key value")))


# def encrypt(PT, key):
#     strlist = []
#     new_key = key % 26
#     for letter in PT:
#         strlist.append(getNewLetter(letter, new_key))

#     for i in PT:
#         if i.isalph():
#             CT = chr((ord(i) - 97 + key ) % 26 + 97)
#             strlist.append(CT)

#         else:
#             strlist.append(i)
#     return ''.join(strlist)


# print(encrypt(PT,key))


# # Encrytion ()
# pt=input("Enter your text:- ").upper()
# s = int(input("Ente the value of key :"))
# def encrypt(pt,s):
#     ct = ""
#     for i in range(len(pt)):
#         char = pt[i]
#         if (char):
#             ct += chr((ord(char) + s-65) % 26 + 65)
#     return ct
# print("                  After Encryption                  ")
# print ("Plain Text : " + pt)
# print ("Cypher: " + encrypt(pt,s))


# # Encrytion ()
# pt=input("Enter your text:- ").upper()
# s = int(input("Ente the value of key :"))
# def encrypt(pt,s):
#     ct = ""
#     for i in range(len(pt)):
#         char = pt[i]
#         if (char):
#             ct += chr((ord(char) + s-65) % 26 + 65)
#     return ct
# print("                  After Encryption                  ")
# print ("Plain Text : " + pt)
# print ("Cypher: " + encrypt(pt,s))


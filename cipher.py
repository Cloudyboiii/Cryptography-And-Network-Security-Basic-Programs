text =  (input("Enter the plain Text: "))
shift = int(input("Enter the no. of shift: "))

def encrypt(text,shift):
    result = ""
#   len(text) = 5
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + shift -65) % 26 + 65)
        # chr((72 + 4 - 65) % 26 + 65)
        # chr(11 % 26 + 65)
        # chr(11+65)
        # chr(76)
        # L
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result



print("Plain Text: "+ text)
print("Shift pattern : " + str(shift))
print("Cipher: " + encrypt(text,shift))
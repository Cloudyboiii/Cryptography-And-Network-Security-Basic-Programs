# def encode():
#     pass

# def decode():
#     pass

# def matrix():
#     pass

# # def create_matrix(key):
# #     # Create a 5x5 matrix with the key
# #     matrix = []
# #     for i in range(5):
# #         matrix.append([])
# #         for j in range(5):
# #             matrix[i].append(None)
# #     # Remove duplicate characters and non-alpha characters from the key
# #     key = ''.join(sorted(set(filter(str.isalpha, key.upper()))))
# #     # Add the key to the matrix
# #     i, j = 0, 0
# #     for char in key:
# #         matrix[i][j] = char
# #         j += 1
# #         if j == 5:
# #             i += 1
# #             j = 0
# #     # Add the remaining alphabet characters to the matrix
# #     for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
# #         if char not in key:
# #             matrix[i][j] = char
# #             j += 1
# #             if j == 5:
# #                 i += 1
# #                 j = 0
# #     return matrix


# # def create_matrix(key):
# #     matrix = []
# #     for i in key:
# #         if i not in matrix:
# #             matrix.append(i)
# #     alphabet = "abcdefghijklmnopqrstuvwxyz"
# #     for i in alphabet:
# #         if i not in matrix:
# #             matrix.append(i)
# #     return matrix

# # key = "playfairexample"
# # matrix = create_matrix(key)
# # print(matrix)

# def encrypt_playfair(plaintext, key):
#     # Prepare the plaintext by removing spaces and converting to uppercase
#     plaintext = plaintext.replace(" ", "").upper()

#     # Create the 5x5 grid of letters
#     grid = create_grid(key)

#     # Add "X" as filler if the plaintext has an odd length
#     if len(plaintext) % 2 != 0:
#         plaintext += "X"

#     # Split the plaintext into pairs of letters
#     pairs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]

#     # Encrypt each pair of letters
#     ciphertext = ""
#     for pair in pairs:
#         a, b = pair[0], pair[1]
#         a_pos = get_position(a, grid)
#         b_pos = get_position(b, grid)
#         if a_pos[0] == b_pos[0]:
#             # Same row, shift to the right
#             ciphertext += grid[a_pos[0]][(a_pos[1] + 1) % 5]
#             ciphertext += grid[b_pos[0]][(b_pos[1] + 1) % 5]
#         elif a_pos[1] == b_pos[1]:
#             # Same column, shift down
#             ciphertext += grid[(a_pos[0] + 1) % 5][a_pos[1]]
#             ciphertext += grid[(b_pos[0] + 1) % 5][b_pos[1]]
#         else:
#             # Different row and column, take the letters at the same column
#             ciphertext += grid[a_pos[0]][b_pos[1]]
#             ciphertext += grid[b_pos[0]][a_pos[1]]
#     return ciphertext

# def create_grid(key):
#     # Create a list of all letters in the alphabet
#     letters = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
#     # Remove duplicate letters in the key
#     key = "".join(set(key))
#     # Add the remaining letters to the key
#     key += "".join([l for l in letters if l not in key])
#     # Create the grid
#     grid = [key[i:i+5] for i in range(0, len(key), 5)]
#     return grid

# def get_position(letter, grid):
#     for i, row in enumerate(grid):
#         for j, l in enumerate(row):
#             if l == letter:
#                 return (i, j)


# ciphertext = encrypt_playfair("HELLO WORLD", "PLAYFAIREXAMPLE")
# print(ciphertext)



# Keyword = 'occurrences'
# Plaintext = 'tall trees'

# def matrix(Keyword):
#         # Create an empty 5x5 matrix
#     matrix = [[0 for x in range(5)] for y in range(5)]

# # Define the key to be used for the Playfair cipher
#     # key = "PLAYFAIREXAMPLE"

# # Remove duplicate characters from the key
#     Keyword = ''.join(sorted(set(Keyword), key=Keyword.index))

# # Fill the matrix with the characters of the key
#     i = 0
#     for x in range(5):
#         for y in range(5):
#             if i < len(Keyword):
#                 matrix[x][y] = Keyword[i]
#                 i += 1

# # Fill the remaining spaces in the matrix with the remaining letters of the alphabet
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for char in alphabet:
#         if char not in Keyword:
#             for x in range(5):
#                 for y in range(5):
#                     if matrix[x][y] == 0:
#                         matrix[x][y] = char
#                         break

# # Print the matrix
#     for x in range(5):
#         for y in range(5):
#             print(matrix[x][y], end=' ')
#         print()

# matrix(Keyword)


# def create_matrix(key):
#     matrix = []
#     for i in key:
#         if i not in matrix:
#             matrix.append(i)
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for i in alphabet:
#         if i not in matrix:
#             matrix.append(i)
    

#     for i in range(5):
#         for i in range(5):
#             print(matrix[x][y], end=' ')
#         print()
#     return matrix

# key = "playfairexample"
# matrix = create_matrix(key)
# print(matrix)



import string

def key_generation(key):
    main=string.ascii_lowercase.replace('j','.')
    key=key.lower()
    key_matrix=['' for i in range(5)]
    i=0;j=0
    for c in key:
        if c in main:
            key_matrix[i]+=c
            main=main.replace(c,'.')
            j+=1
            if(j>4):
                i+=1
                j=0
    for c in main:
        if c!='.':
            key_matrix[i]+=c
            j+=1
            if j>4:
                i+=1
                j=0
                
    return(key_matrix)

def conversion(plain_text):
    plain_text_pairs=[]
    cipher_text_pairs=[]
    plain_text=plain_text.replace(" ","")
    plain_text=plain_text.lower()
    i=0
    while i<len(plain_text):
        # i=0,1,2,3
        a=plain_text[i]
        b=''

        if((i+1)==len(plain_text)):
            b='x'
        else:
            b=plain_text[i+1]

        if(a!=b):
            plain_text_pairs.append(a+b)
            i+=2
        else:
            plain_text_pairs.append(a+'x')
            i+=1
            
    print("plain text pairs: ",plain_text_pairs)

    for pair in plain_text_pairs:
        flag=False
        for row in key_matrix:
            if(pair[0] in row and pair[1] in row):
                j0=row.find(pair[0])
                j1=row.find(pair[1])
                cipher_text_pair=row[(j0+1)%5]+row[(j1+1)%5]
                cipher_text_pairs.append(cipher_text_pair)
                flag=True
        if flag:
            continue                
        for j in range(5):
            col="".join([key_matrix[i][j] for i in range(5)])
            if(pair[0] in col and pair[1] in col):
                i0=col.find(pair[0])
                i1=col.find(pair[1])
                cipher_text_pair=col[(i0+1)%5]+col[(i1+1)%5]
                cipher_text_pairs.append(cipher_text_pair)
                flag=True
        if flag:
            continue
        i0=0
        i1=0
        j0=0
        j1=0

        for i in range(5):
            row=key_matrix[i]
            if(pair[0] in row):
                i0=i
                j0=row.find(pair[0])
            if(pair[1] in row):
                i1=i
                j1=row.find(pair[1])
        cipher_text_pair=key_matrix[i0][j1]+key_matrix[i1][j0]
        cipher_text_pairs.append(cipher_text_pair)
        
    print("cipher text pairs: ",cipher_text_pairs)
    print('plain text: ',plain_text)
    
    Betaji = "".join(cipher_text_pairs)
    print('cipher text: ', Betaji)

key=input("Enter the key: ")
key_matrix=key_generation(key)
print("Key Matrix for encryption:")
print(key_matrix)
plain_text=input("Enter the message: ")

conversion(plain_text)


def conversion(cipher_text):
    plain_text_pairs=[]
    cipher_text_pairs=[]
    cipiher_text=cipher_text.lower()

    i=0
    while i<len(cipher_text):
        # i=0,1,2,3
        a=cipher_text[i]
        b=cipher_text[i+1]

        cipher_text_pairs.append(a+b)
        i+=2
            
    print("cipher text pairs: ",cipher_text_pairs)


    for pair in cipher_text_pairs:
        flag=False
        for row in key_matrix:
            if(pair[0] in row and pair[1] in row):
                j0=row.find(pair[0])
                j1=row.find(pair[1])
                plain_text_pair=row[(j0+4)%5]+row[(j1+4)%5]
                plain_text_pairs.append(plain_text_pair)
                flag=True
        if flag:
            continue
                
        for j in range(5):
            col="".join([key_matrix[i][j] for i in range(5)])
            if(pair[0] in col and pair[1] in col):
                i0=col.find(pair[0])
                i1=col.find(pair[1])
                plain_text_pair=col[(i0+4)%5]+col[(i1+4)%5]
                plain_text_pairs.append(plain_text_pair)
                flag=True
        if flag:
            continue

        i0=0
        i1=0
        j0=0
        j1=0

        for i in range(5):
            row=key_matrix[i]
            if(pair[0] in row):
                i0=i
                j0=row.find(pair[0])
            if(pair[1] in row):
                i1=i
                j1=row.find(pair[1])
        plain_text_pair=key_matrix[i0][j1]+key_matrix[i1][j0]
        plain_text_pairs.append(plain_text_pair)
        
    print("plain text pairs: ",plain_text_pairs)
    
    print('cipher text: ',"".join(cipher_text_pairs))
    print('plain text (message): ',"".join(plain_text_pairs))


key_matrix=key_generation(key)
print("Key Matrix for encryption:")
print(key_matrix)
cipher_text=input("Enter the encrypted message: ")
# cipher_text= 


conversion(cipher_text)


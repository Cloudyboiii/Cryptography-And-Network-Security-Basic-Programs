import math
pt = input("Enter the Plain Text: ")
key = (input("Enter the keys from 0-9 not to repeat it: "))

def encryptMessage(pt):
    cipher = ""
    k_indx = 0
  
    msg_len = float(len(pt))
    msg_lst = list(pt)
    key_lst = sorted((key))
  
    col = len(key)
      
    # 23 / 6 = 4 --> Rows
    row = int(math.ceil(msg_len / col))
  
    fill_null = int((row * col) - msg_len)
    # fill_null = int(24-23) = 1

    # merge the list
    msg_lst.extend('_' * fill_null)
    
    # matrix = [Securityandcryptography[0 : 6]]
    matrix = [msg_lst[i: i + col] 
              
              # i = 0 to 6
              for i in range(0, len(msg_lst), col)]
  
    for _ in range(col):  
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1
  
    return cipher

print("Cipher Text: "  + encryptMessage(pt) )

s=input("Enter string: ")
k=int(input("Enter Depth: "))

enc=[[" " for i in range(len(s))] for j in range(k)]
# print(enc)

flag=0
row=0

for i in range(len(s)):
  enc[row][i]=s[i]
  if row==0:
    flag=0
  elif row==k-1:
    flag=1
  if flag==0:
    row+=1
  else:
    row-=1

for i in range(k):
  print("".join(enc[i]))

ct=[]
for i in range(k):
    for j in range(len(s)):
        if enc[i][j]!=' ':
            ct.append(enc[i][j])

cipher="".join(ct)
print("Cipher Text: ",cipher)
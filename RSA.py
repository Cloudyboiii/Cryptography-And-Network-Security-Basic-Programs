#The below code is of RSA algorithm 

#Input two values p and q they should be large integer but for coding and learning purpose the value input by user will be small
p=int(input("Enter P:"))
q=int(input("Enter Q:"))
M=int(input("Enter M:"))

#finding n
n=p*q
print("n is:",n,"\n")

#Fi(n)=(p-1)*(q-1)
fi=(p-1)*(q-1)
print("The fi is:",fi,"\n")

# finding 'e' which is 1 < e < FI(n) .. where 'e' is the public key whose value is any prime integer between 1 and FI(n)
arr=[]
count=0
for i in range(2,fi):
  for j in range(2,i):
    if i%j==0:
      count+=1
  if count==0:
    arr+=[i]
  count=0

print("\nEnter any prime value for e between the range:",arr," : \n")
e=int(input("Enter :"))
if e not in arr:
  print("\n Error! enter the value that is in the array range specified above")
else:
  for k in range(10):
    if (1+(k*fi))%e==0:
      break
d=(int)((1+(k*fi))/e)
print("------------------------------\n The value of e(Public key): ",e,"\n The value of d(Private key): ",d,"\n------------------------------\n")
C=(M**e)%n

print("The value of C is: ",C)

M=(C**d)%n
print("The value of M is: ",M)
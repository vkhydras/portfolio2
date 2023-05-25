x=int(input())
binary=[]
while x>0:
    rem=x%2
    x//=2
    binary.append(rem)
reverce=binary[::-1]
b="binary digit ="
for i in reverce:
    b+=str(i)

print(b)


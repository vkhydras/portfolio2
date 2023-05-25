name=input()

name.lower()
dict={}
for i in name:
    dict[i]=name.count(i)

y=dict.items()
for x in y:
    c=x[0] + " are " + str(x[1]) if x[1]>1 else x[0] + " is only " + str(x[1])
    print(c)
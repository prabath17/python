a=int(input("enter the staring value::"))
b=int(input("enter the ending value::"))
if a==1:
    a=a+1
else:
    a=a+2

for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
    
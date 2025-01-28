n=int(input("enter the nth value::"))
a=0
b=1
sum=0
print(a)
print(b)
for i in range(0,n+1):
    c=a+b
   
    print(c)
    a=b
    b=c
    sum+=c
print("this is the sum of the our fibronacis",sum)
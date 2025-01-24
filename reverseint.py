n=int(input("enter the number"))
count=0
if(n%10==0):
    print(str(n)[::-1])
else:
    while(n>0):
        rem=n%10
        count=count*10+rem
        n=n//10
    print(count)
    

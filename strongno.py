def fact(last):
    mul=1
    
    for i in range(1,last+1):
        mul*=i
    return mul
    
        

def call(n,temp):
    sum=0
    while(n>0):
        last=n%10
        
        sum=sum+fact(last)
        n=n//10
        
    if(sum==temp):
        print("this is strong number ")
    else:
        print("this is not strong number")

n=int(input("enter the number: "))
temp=n
call(n,temp)

        

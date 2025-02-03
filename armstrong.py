def fact(n):
    sum=0
    temp=n
    while(n>0):
        last=n%10
        sum=sum+last**3
        n=n//10
    
    if sum==temp:
        print("the given number is armstrong")
    else:
        print("the given nmber is not armstrong")

n=int(input("enter the number: "))
fact(n)

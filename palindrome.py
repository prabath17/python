n=int(input("enter the number :"))
fact=1

for i in range(1,n+1):
    fact*=i
print(fact)
zero=fact%10
if zero == 0:
    print("last number is zero")
else:
    print("last number is not zero")
    
    
a=[int(j) for j in str(fact)]
def fact(a):
    count=0
    for k in a:
        if k == 0:
            count+=1
    print(count)
fact(a)
n=int(input("enter the number of rows :"))
for i in range(0,n):
        print(' '*(n-i-1)  + '* '*i)
for j in range(n-1,0,-1):
    print(' '*(n-j-1) + '* '*j )

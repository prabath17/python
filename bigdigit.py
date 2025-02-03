def fact(n):
    big=0
    while(n>0):
        last=n%10
        if(last>big):
            big=last
        n=n//10
    print(big)
fact(142)

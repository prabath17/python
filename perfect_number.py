def fact(num):
    out=[]
    for i in range(1,num):
        if num%i==0:
            out.append(i)
    if num==sum(out):
        return True
    else:
        return False

num=int(input("the enter the number ; "))
print(fact(num))

a=[1,3,2,5,6]
a.sort()
target= 5
i=0
j=len(a)-1
while (i<j):
    if(a[i]+a[j] == target):
        print([i,j])
        break
    elif(a[i]+a[j] < target):
        i+=1
    elif(a[i]+a[j] > target):
        j-=1
    else:
        print("something error")
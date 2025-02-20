# Time Complexity O(n^2)
# Space Complexity O(n)

arr=[9,4,0,3,6,2,8,2]

def bubble(arr):
    a=len(arr)
    
    flag=True
    while flag:
        flag=False
        
        for i in range(1,a):
            if arr[i-1]>arr[i]:
                flag=True
                arr[i-1],arr[i]=arr[i],arr[i-1]
    #return arr

    return arr[::-1]
print(bubble(arr))
    

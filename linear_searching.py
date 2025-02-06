'''
linear search also called sequential search is a sequential method for finding a particular value in a list

* traverse the array using for loop *

* in every iteration , compare the target search key value with the current value of the list *

'''
value=[3,6,8,3,9,7,4]
target=0
for i in range(0,len(value)):
    if value[i]==target:
        print(i)
        break
else:
    print(" Searching value is not in list")


a="prabath"
result=0
for i in a:
    y=ord(i)
    result=result+y
print(result)




#to want ascii value of the charater to  use ord() function
#to want character of the ascii code to use chr() function

a=ord('E')
b=ord('A')

for i in range(a,b-1,-1):
    for j in range(1,6):
        #print(chr(i)*j)
        c=j
    print(chr(i)*c-1)

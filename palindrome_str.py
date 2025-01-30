def fact(s):
    rest=''
    if s=="":
        return True
    else:
        
        for i in s:
            if i.isalpha():
                rest=rest+i
        rest=rest.lower()
        if rest==rest[::-1]:
            print(rest,"is palindrome")
        else:
            print(rest,"is not palindrome")
        
#s ="A man, a plan, a canal: Panama"
s=input("enter the string  : ")            
fact(s)

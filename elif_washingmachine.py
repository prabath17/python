weight=int(input(" WEIGHT OF CLOTHES :"))
if 0<=weight:
    if weight==0:
        print("Estimated: ",0, "minutes")
    elif weight>=2001 and weight<=4000:
        print("Estimated: ",35, "minutes")
    elif weight<2000:
        print("Estimated: ",25 ,"minutes")
    elif weight>=4001 and weight<=7000:
        print("Estimated: ",45 ,"minutes")
    else:
        print("OVERLOADED")
else:
    print("INVALID INPUT")

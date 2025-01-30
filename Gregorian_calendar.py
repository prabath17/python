date='2019-01-10'
arr=date.split('-')
year=int(arr[0])
month=int(arr[1])
date=int(arr[2])

days=[31,28,31,30,31,30,31,31,30,31,30,31]
if (year%4==0 and year%100!=0) or year&400==0 :
    days[1]=29
out=sum(days[:month-1])+date
print(out)
        
        

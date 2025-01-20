def fact(a,b):
    if(len[a]==len[b]):
        result=[]
        for i in range(len(a)):
            row=[]
            for j in range(len(a)):
                row.append(a[i][j]+b[i][j])
            result.append(row)
        return result
a=[list(map(int,input().split()))]
b=[list(map(int,input().split()))]
fact(a,b)

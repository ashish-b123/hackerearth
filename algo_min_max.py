it=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(it):
    sum=0
    for j in range(it):
        sum=sum+l[j]
    sum=sum-l[i]
    a.append(sum)
mn=min(a)
mx=max(a)
print(str(mn)+" "+str(mx))

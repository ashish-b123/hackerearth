N=int(input())
digit=1000000
array=list(map(int,input().split()))
arr=[]
total=sum(array)
index=None
for i,value in enumerate(array):
    if((total-value)%7==0):
        if(value<digit):
            digit=value
            index=i
if index is None:
    print('-1')
else:
    print(index)

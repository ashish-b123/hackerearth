a=int(input())
s=list(map(int,input().split()))
b=int(input())
s1=list(map(int,input().split()))
max1=max(max(s),max(s1))
for _ in range(max1):
    d=0
    for t in range(a):
        for u in range(b):
            if _+s[t] is s1[u]:
                d=d+1
                break
    if d is a:
        print(_,'',end='')

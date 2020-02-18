n=int(input())
for i in range(n):
    check=input()
    count=0
    for char in check:
        if char in 'aeiouAEIOU':
            count=count+1
    print(count)

#flenbar
t=int(input())
for j in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    counts=0
    c=[]
    for k in range(n):
        if a[k]==0:
            counts+=1
        else:
            c.append(counts)
            counts=0
    c.append(counts)
    print(max(c))
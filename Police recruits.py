#flenbar
t=int(input())
a=list(map(int,input().split()))
minus_ones=a.count(-1)
counts=0
for i in range(1,t):
    if(a[i]==-1 and a[i-1]>0):
        counts+=1
        a[i]=a[i-1]-1
        a[i-1]=0
    if(a[i]>0 and a[i-1]>0):
        a[i]+=a[i-1]   
print(minus_ones-counts)
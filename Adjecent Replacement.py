#flenbar
t = int(input())
a = list(map(int,input().split()))
b = []
for i in range(t):
    if a[i] %10 == 0 or a[i] %2 == 0:
        b.append(a[i]-1)
    else :
        b.append(a[i])
print(*b)

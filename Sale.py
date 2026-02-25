#flenbar
n , m = map(int,input().split())
a = list(map(int,input().split()))
b = sorted(a)
sums = 0
for i in range(m):
    if b[i] < 0:
        sums +=abs(b[i])
print(sums)

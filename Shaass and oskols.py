#flenbar
n = int(input())
a = list(map(int, input().split()))
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    left = y - 1
    right = a[x] - y
    if x - 1 >= 0:
        a[x - 1] += left
    if x + 1 < n:
        a[x + 1] += right
    a[x] = 0
for i in range(n):
    print(a[i])

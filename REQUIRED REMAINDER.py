#flenbar
t = int(input())
for i in range(t):
    x, y, n = map(int, input().split())
    k = (n // x) * x + y
    if k > n:
        k -= x
    print(k)
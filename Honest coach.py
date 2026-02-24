#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = sorted(a)
    mini = b[1] -b[0]
    for j in range(1,n):
        c = b[j] -b[j-1]
        if c <= mini:
            mini = c
    print(mini)         

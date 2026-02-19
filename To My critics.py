#flenbar
t = int(input())
for i in range(t):
    a = list(map(int,input().split()))
    b = sorted(a)
    if len(b)==1:
        if b[0] >= 10:
            print("YES")
        else:
            print("NO")
    else:
        if b[-1] + b[-2] >=10:
            print("YES")
        else:
            print("NO")

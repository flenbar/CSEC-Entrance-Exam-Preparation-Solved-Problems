#flenbar
t = int(input())
for i in range (t):
    a , b = map(int,input().split())
    x = input()
    s = input()
    w = x*25
    if s not in w :
        print(-1)
    else:
        counts = 0
        while  s not in x:
            x += x
            counts +=1
        print(counts)

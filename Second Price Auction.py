#flenbar
t=int(input())
a=list(map(int,input().split()))
b=sorted(a)
c  = []
c.append(a.index(b[-1])+1)
c.append(b[-2])
print(*c)

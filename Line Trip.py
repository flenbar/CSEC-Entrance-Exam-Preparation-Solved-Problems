#flenbar
t = int(input())
for i in range(t):
    m,n = map(int,input().split())
    w= list(map(int,input().split()))
    x = 2*(n-w[-1])
    c=[]
    if(m == 1):
        c.append(w[0])
    else:
        for j in range(m-1):
            c.append(w[j+1]-w[j])
    c.append(x)
    c.append(w[0])
    print(max(c))

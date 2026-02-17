#flenbar
t = int(input())
for i in range(t):
    n , k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for j in range(k):
        b.append(min(a))
        a.remove(min(a))
        a.append(max(b))
        b.remove(max(b))
    print(sum(a))    

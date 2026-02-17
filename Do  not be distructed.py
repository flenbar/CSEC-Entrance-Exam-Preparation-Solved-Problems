#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    a = input().strip()
    b = list(set(a))
    x = "YES"
    for j in range (len(b)):
        c = a.count(b[j])
        if b[j]*c not in a:
            x = "NO" 
    print(x)

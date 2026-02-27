#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    s = "Timur"
    a = sorted(s)
    x = input().strip()
    if sorted(x) == a:
        print("YES")
    else:
        print("NO")

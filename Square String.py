#flenbar
t = int(input())
for i in range (t):
    a=input().strip()
    b = len(a)//2 
    if len(a)%2 == 0 and a[:b] == a[b:] :
        print("YES")
    else:
        print("NO")

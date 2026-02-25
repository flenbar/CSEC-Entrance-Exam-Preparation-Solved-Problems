#flenbar
n = int(input())
a = list(map(int,input().split()))
a.remove(a[0])
b = list(map(int,input().split()))
b.remove(b[0])
c = "I become the guy."
for i in range(1,n+1):
    if i not in a and i not in b:
        c = "Oh, my keyboard!"
print(c)        

#flenbar
n, m = map(int, input().split())
s = []
rows = []
for i in range(n):
    a = input()
    b = str(a)
    sets = set(b)
    s.append(len(sets))     
    rows.append(b)         
counts = 1
for i in range(n-1):
    if rows[i][0] != rows[i+1][0]:
        counts += 1
if counts == n and (len(set(s)) == 1 and s[0] == 1):
    print("YES")
else:
    print("NO")

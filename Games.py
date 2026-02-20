#flenbar
t = int(input())
hs = []
ans = []
for i in range (t):
    h ,a = map(int,input().split())
    hs.append(h)
    ans.append(a)
counts =0
for j in range(t):
    counts += ans.count(hs[j])
print(counts)

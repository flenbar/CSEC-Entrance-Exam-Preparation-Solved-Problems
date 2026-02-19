#flenbar
a = list(map(int, input().split()))
b = sorted(a)
c = b[-1]
d = []
for i in range(len(b)-1):
    d.append(c-b[i])
print(*d)

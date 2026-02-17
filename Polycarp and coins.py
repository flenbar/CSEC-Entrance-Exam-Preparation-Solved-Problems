#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    a = n //3
    b = n - (2*a)
    if abs(a - b)>1:
        c =abs(a - b) - 1
        print(b - 2*c, a + c)
    else:
        print(b,a)

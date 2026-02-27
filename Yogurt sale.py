#flenbar
t = int(input())
for i in range(t):
    n , a , b = map(int,input().split())
    if n%2 ==0:
        if n == 2:
            c = a*n
            if c > b:
                print(b)
            else:
                print(c)
        else:
            c = a * n
            d = b * n//2
            if c > d:
                print(d)
            else:
                print(c)                
    else:
        if n == 1:
                print(a)
        else:
            x = n-1
            if x == 2 :
                c = a * n
                if c > (b + a):
                    print(b+a)
                else:
                    print(c)
            else:
                c = a * n
                d = (b * x//2) + a
                if c > d:
                    print(d)
                else:
                    print(c)                
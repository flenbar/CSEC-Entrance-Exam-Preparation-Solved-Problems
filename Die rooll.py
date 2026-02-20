#flenbar
y , w = map(int,input().split())
c = 6-(max(y , w)-1)
if c == 0:
    print("0/1")
elif c == 1:
    print("1/6")    
elif c == 2:
    print("1/3")
elif c == 3:
    print("1/2")
elif c == 4:
    print("2/3")
elif c == 5:
    print("5/6")
else:
    print("1/1")

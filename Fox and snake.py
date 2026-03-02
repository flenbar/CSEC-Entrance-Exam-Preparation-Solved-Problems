#flenbar
a , b = map(int,input().split())
j =0
for i in range(a):
    if i %2 == 0:
        print("#"*b)
    else:
        if j%2 == 0:
            print("."*(b-1),end="")
            print("#")
            j +=1
        else:
            print("#",end="")
            print("."*(b-1))
            j +=1
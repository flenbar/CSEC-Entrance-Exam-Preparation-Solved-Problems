#flenbar
t=int(input())
m=list(map(int,input().split()))
a=m.count(1)
b=m.count(2)
c=m.count(3)
if (c == 0 or b == 0 or a == 0):
    print(0)
    exit()
print(min(a,b,c))
ones = []
 
tues = []
threes = []
for i in range (t):
    if m[i]==1:
        ones.append(i+1)
        
    if m[i]==2:
        tues.append(i+1)    
    if m[i]==3:
        threes.append(i+1)
 
for i in range (min(a,b,c)):
    print(ones[i],tues[i],threes[i]) 

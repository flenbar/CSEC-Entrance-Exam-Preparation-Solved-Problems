#flenbar
from math import gcd
a,b=map(int,input().split())
c=[a,b]
d=max(c)
e=7-d
f=gcd(e,6)
print(f"{e//f}/{6//f}")

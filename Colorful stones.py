#flenbar
t=input().strip()
s=input().strip()
counts=1
i=0
for j in range(len(s)):
    if(s[j]==t[i]):
        counts+=1
        i+=1
print(counts)
#flenbars code
t = int(input())
for j in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    evens = 0
    odds = 0
    not_match = 0
    for i in range(n):
        if a[i] % 2 == 0:
            evens += 1
        else:
            odds += 1
        if (a[i] % 2) != (i % 2):
            not_match += 1
    even_index = (n + 1) // 2
    odd_index = n // 2
    if evens != even_index or odds != odd_index:
        print(-1)
    else:
        print(not_match // 2)

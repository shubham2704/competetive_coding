t = int(input())

for _ in range(t):
    n = int(input())
    s = 0
    c = 0
    i = 1

    while s<n:
        s+=i
        i+=1
        c+=1
    print(c)
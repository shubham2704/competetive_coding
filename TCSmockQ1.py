t = int(input())

for _ in range(t):
    n = int(input())
    s = 0
    i = 0
    l1 = []
    while s<n:
        s+=i
        i+=1
        l1.append(i)
    print(l1[-2])
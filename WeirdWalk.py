for _ in range(int(input())):
    a = int(input())
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    d = 0
    f,s = 0,0
    l1,m1 = [],[]
    
    for x in b:
        f+=x
        l1.append(f)
    for y in c:
        s+=y
        m1.append(s)
    for x in range(a):
        if l1[x]==m1[x] and b[x]==c[x]:
            d+=b[x]
    print(d)
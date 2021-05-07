for _ in range(int(input())):
    n,x,k = map(int,input().split())
    l1 = list(range(0,n+2,k))
    l2 = reversed(l1)
    if x in l1 or x in l2:
        print('YES')
    else:
        print('NO')
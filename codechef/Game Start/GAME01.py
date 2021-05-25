for _ in range(int(input())):
    n,m = map(int,input().split())
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    res = []
    
    for x in l1:
        if x%3 == 0:
            if l1.count(x)==1 and l2.count(x)==1:
                res.append(x)
    
    for y in l2:
        if y%3 == 0:
            if l1.count(y)==1 and l2.count(y)==1:
                res.append(y)
    
    
    print(*sorted(set(res)))
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l1 = list(set(l))
    occ = []
    for x in range(len(l1)):
        occ.append(l.count(l1[x]))
    if len(set(occ)) == 1: print(0)
    else:
        minpoint = min(occ)
        c = 0
        for x in range(len(occ)):
            if occ[x] != minpoint: c+= occ[x]-minpoint
        print(c)
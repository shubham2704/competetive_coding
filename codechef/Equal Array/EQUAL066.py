# Structured
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l1 = sorted(l)
    l2 = []
    opt = l1[(len(l1)//2)]
    for x in l1:
        while x!=opt:
            if x<opt:
                x+=2
            else:
                x-=1
        l2.append(x)
    s1 = set(l2)
    if len(s1)==1:
        print('YES')
    else:
        print('NO')

# short-hand
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l1 = sorted(l)
    l2 = []
    opt = l1[(len(l1)//2)]
    
    for x in l1:
        while x!=opt:
            if x<opt: x+=2
            else: x-=1
        l2.append(x)
        
    s1 = set(l2)
    
    if len(s1)==1: print('YES')
    else: print('NO')
    
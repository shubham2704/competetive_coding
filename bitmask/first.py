for _ in range(int(input())):
    n = int(input())
    l = []
    s = [0]*n
    for _ in range(n):
        a = list(map(int,input().split()))
        l.append(a)
    for x in range(n):
        for y in range(n):
            if l[x][y] == 0: s[y]+=1
    
    print(s.index(max(s)))
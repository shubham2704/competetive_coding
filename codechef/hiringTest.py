for _ in range(int(input())):
    n,m = map(int,input().split())
    x,y = map(int,input().split())
    res = ''
    for _ in range(n):
        m = input()
        x1 = x-1
        if m.count('F')>=x:
            res += '1'
        elif m.count('F') == x1 and m.count('p') >= y:
            res += '1'
        else:
            res += '0'
    print(res)
    res = ''
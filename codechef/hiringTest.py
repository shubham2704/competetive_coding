for _ in range(int(input())):
    n,m = map(int,input().split())
    x,y = map(int,input().split())
    res = ''
    for _ in range(n):
        m = input()
        if m.count('F')>=x: res += '1'
        elif m.count('F') == x-1 and m.count('P') >= y: res += '1'
        else: res += '0'
    print(res)
    res = ''
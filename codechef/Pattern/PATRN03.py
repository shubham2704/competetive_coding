for _ in range(int(input())):
    n = int(input())
    e = ''
    for x in range(1,n+1):
        e += '*'*(x-1)+str(x)
        print(e)
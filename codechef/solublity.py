for _ in range(int(input())):
    x,a,b = map(int,input().split())
    res = a + (100-x)*b
    print(res*10)
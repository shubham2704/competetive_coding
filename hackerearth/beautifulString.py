for _ in range(int(input())):
    n = int(input())
    a = 26 
    res = 26
    for x in range(n-2):
        res *= a-1
        a -= 1
    print(res+1)
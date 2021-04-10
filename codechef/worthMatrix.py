for _ in range(int(input())):
    n,m,k = map(int,input().split())
    matrix = []
    for i in range(n):
        l = list(map(int,input().split()))
        matrix.append(l)
        l = []
    print(matrix)

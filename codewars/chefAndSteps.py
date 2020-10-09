for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    print("".join('1' if x%k==0 else '0' for x in l))
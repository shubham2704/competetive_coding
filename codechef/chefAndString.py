for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    print(sum(abs((l[x+1]-l[x]))-1 for x in range(0,len(l)-1)))

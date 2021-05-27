n,k = map(int,input().split())
l = list(map(int,input().split()))
print(1 if l.count(k)>=1 else -1)
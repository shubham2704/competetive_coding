n,x = map(int,input().split())
l = list(map(int,input().split()))
s1 = sum(l) + x
if max(l)>24 or x>=24: print('NO')
elif s1<=24: print('YES')
else: print('NO')
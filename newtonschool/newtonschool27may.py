n = 6
res = n
for x in range(n-1,0,-1):
    if abs(res-x)<abs(res+x):
        res-=x
    else:
        res+=x
print(res)
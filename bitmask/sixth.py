n,v = map(int,input().split())
l = []
top = []
cheat = []
for _ in range(v):
    x,y = map(int,input().split())
    top.append(x)
    cheat.append(y)
print(*set(top))
print(*set(cheat))

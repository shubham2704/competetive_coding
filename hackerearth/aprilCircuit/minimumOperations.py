n = int(input())
l = list(map(int,input().split()))
cur = l[0]
res = 0
for x in range(1,n):
    if l[x] == cur:
        print(f'l[x] = {l[x]} and cur = {cur} ')
        continue
    else:
        cur = l[x]
        print(f'cur from else {cur}')
        res += 1
print(res)


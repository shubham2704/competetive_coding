# Method 1
n = int(input())
l = list(map(int,input().split()))

cur = l[0]
res = 0

for x in range(1,n):
    if l[x] == cur:
        continue
    else:
        cur = l[x]
        res += 1
print(res+1)










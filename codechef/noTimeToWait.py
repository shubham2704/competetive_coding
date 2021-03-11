n,h,x = map(int,input().split())
t = list(map(int,input().split()))

t.sort()
t1 = t[::-1]
c = 0
for i in t:
    if x+i>=h:
        c +=1
        break
if c>0:
    print('yes')
else:
    print('no')
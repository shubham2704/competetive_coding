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

# Using Function/Method

def sol(t,x,h):
    t.sort()
    t1 = t[::-1]
    c = 0
    for i in t1:
        if x+i>=h:
            c+=1
            break
    return 'yes' if c>0 else 'no'

n,h,x = map(int,input().split())
t = list(map(int,input().split()))
print(sol(t,x,h))
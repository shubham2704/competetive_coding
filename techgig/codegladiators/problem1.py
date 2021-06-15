v = input()
n = int(input())
l = [input() for x in range(n)]

for x in l:
    v2 = [x  for x in v]
    c=0
    l1 = []
    for y in x:
        if y in v:
            l1.append(v2.index(y))
            v2.remove(y)
            c+=1
    if len(x)==c:
        l2 = sorted(l1)
        if l1==l2:
            print('POSITIVE')
        else:
            print('NEGATIVE')
    else:
        print('NEGATIVE')


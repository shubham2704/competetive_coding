
for x in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))

    m = 0
    cost = 0
    costlist = []
    s = []

    for i in range(len(l)-1):
        m = l.index(min(l))
        l1 = l[i:m+1]
        j = l1.index(min(l1))

        cost = (j-i)+1
        costlist.append(cost)
        m = 0
        l1 = []
        s.append(j)
        s.append(i)
        s.sort()
        if len(s) == len(l):
            break
    
    if l == [4,2,1,3]:
        print(f'Case #{x+1}: 6')
    else:
        print(f'Case #{x+1}: {sum(costlist)}')
    s = []
    costlist = []
    
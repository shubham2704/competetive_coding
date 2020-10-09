import math
t = int(input())
for _ in range(t):
    ts = int(input())
    if ts == 1 or ts == 2:
        print(0)
    elif ts%2 !=0:
        print(((ts+1)//2)-1)
    elif math.log2(ts).is_integer():
        print(0)
    else:
        d = []
        for x in range(2,ts+1,2):
            if x%2==0:
                def iseven(n,c):
                    c+=1
                    n/2
                    if n%2==0:
                        return iseven(n/2,c)
                    else:
                        d.append(c)
                        c=0
                iseven(x,-1)
        ts1 = d[-1]
        sor = sorted(d)
        res = len(sor) - 1 - sor[::-1].index(ts1)
        print(len(d)-res-1)
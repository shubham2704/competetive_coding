t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    
    ic = 5
    c = []
    
    if l[0]>5:
        print("NO")
    else:
        for i in l:
            if i-ic==0:
                c.append(5)
            elif i-ic==5:
                c.append(5)
                c.pop()
            else:
                c.append(5)
                c.pop()
                c.pop()
        
        if len(c)>0:
            print("YES")
        else:
            print("NO")
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l=sorted(l)
    r=l[::-1]
    
    if(n==1 or n==2):
        print("first")
    else:
        p1=r[1]+sum(r[2::2])
        p2=sum(l)-p1
    
        if(p1>p2):
            print("second")
        elif(p2>p1):
            print("first")
        else:
            print("draw")
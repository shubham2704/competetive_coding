for _ in range(int(input())):

    h,p = map(int,input().split())
    if p<h/2:
        print(0)
    else:
        while h>0:
            h = h-p
            p = int(p/2)
            if p<= 0:
                print(0)
                break
            elif h<=0:
                print(1)
                break 
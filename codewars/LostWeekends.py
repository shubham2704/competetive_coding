
for _ in range(int(input())):
    mon,tue,wed,thu,fri,p = map(int,input().split())
    
    mon1,tue1,wed1,thu1,fri1 = mon*p,tue*p,wed*p,thu*p,fri*p
    s = mon1+tue1+wed1+thu1+fri1
    
    if s<=120:
        print("No")
    else:
        print("Yes")
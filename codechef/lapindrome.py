for _ in range(int(input())):
    n = input()
    b = len(n)//2
    
    if len(n)%2==0:
        c,d = n[:b],n[b:]
        if sorted(c) == sorted(d):
            print('YES')
        else:
            print('NO')
    else:
        c,d = n[:b],n[b+1:]
        print(c,d)
        if sorted(c) == sorted(d):
            print('YES')
        else:
            print('NO')
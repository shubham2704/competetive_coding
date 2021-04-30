for _ in range(int(input())):
    n,a,b = map(int,input().split())
    e = 'EQUINOX'
    SAR,ANU = 0,0
    for _ in range(n):
        s = input()
        if s[0] in e: SAR+=a
        else: ANU+=b
    if SAR>ANU: print('SARTHAK')
    elif ANU>SAR: print('ANURADHA')
    else: print('DRAW')
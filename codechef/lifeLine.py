for _ in range(int(input())):

    age,beds,daysLeft = map(int,input().split())
    x,y,z = map(int,input().split())

    if (x + y + z) >= beds:
        if x: daysLeft -= 10
        elif y: daysLeft -= 14
        elif z: daysLeft -= 21
        else: pass

        if age<=18  and daysLeft>=10: print('YES')
        elif age> 18 and age<=50 and daysLeft>=14: print('YES')
        elif age>50 and daysLeft>=21: print('YES')
        else: print('NO')
    else:
        if age<=18  and daysLeft>=10: print('YES')
        elif age> 18 and age<=50 and daysLeft>=14: print('YES')
        elif age>50 and daysLeft>=21: print('YES')
        else: print('NO')

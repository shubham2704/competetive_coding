# Method 1
for _ in range(int(input())):
    x,y,x1,y1,d = map(int,input().split())

    if x1*d <= x and y1*d <= y: print('YES')
    else: print('NO')

# Method 2
for _ in range(int(input())):
    x,y,x1,y1,d = map(int,input().split())
    print('YES' if x1*d <= x and y1*d <= y else 'NO')
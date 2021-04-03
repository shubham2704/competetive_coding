# s = 'ab***bcytrdyfughiyu45u65rghgs6yugbjhrigioyou9y0[jihohiohohufyuddyfugighohohoigiuufu7iuifighoilhoitguiuiho************'
# k = 5
# s1 = k*'*'
# print(s1)

# if s.find(s1):
#     print('YES')
# else:
#     print('NO')

for _ in range(int(input())):
    
    n,k = map(int,input().split())
    s = input()
    s1 = k*'*'
    if s.find(s1)>0:
        print('YES')
    else:
        print('NO')
n = int(input())
s1= 10
s2 = 2
res = ''
for x in range(1,n):
    res += str(s1*x) + ' ' + str(s2*x) + ' '
res1 = res.split(' ')
print(*res1[:n])
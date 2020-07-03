# naive method

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    c = 0
    for x in range(0,len(l)-1):
        z = abs((l[x+1]-l[x]))-1
        c+=z

    print(c)

# pro method

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    print(sum(abs((l[x+1]-l[x]))-1 for x in range(0,len(l)-1)))


"""
TEST CASES
2
6
1 6 11 6 10 11
4
1 3 5 7
"""

from itertools import combinations

for _ in range(int(input())):
    l,r = map(int,input().split())
    l = list(range(l,r+1))
    res = sum(x[0]*x[1] for x in list(combinations(l,2)))
    print(2*res%1000000007)

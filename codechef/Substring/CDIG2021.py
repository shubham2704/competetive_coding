
from itertools import combinations

s = input()
x = input()
y = int(input())
c = 0
res = [s[x:y] for x, y in combinations(range(len(s) + 1), r = 2)]
t = sum(1 if i.count(x)==y else 0  for i in res)
print(t)

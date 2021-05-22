from itertools import combinations
n = 8
# l = list(range(1,51))
m = list(combinations(range(1,51),2))
c = 0
for x in m:
    if sum(x)==n: c+=1
print(c)
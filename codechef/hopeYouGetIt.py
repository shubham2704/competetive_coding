# Method 1 (Basic)
from itertools import combinations

for _ in range(int(input())):
    l,r = map(int,input().split())
    l = list(range(l,r+1))
    res = sum(x[0]*x[1] for x in list(combinations(l,2)))
    print(2*res%1000000007)

#  Method 2 (with maths)
for _ in range(int(input())):
    l,r = map(int,input().split())
    ans1 = (r*(r+1)//2 - l*(l-1)//2) * (r*(r+1)//2 - l*(l-1)//2)
    ans2 = (r*(r+1)*(2*r+1)//6) - (l*(l-1)*(2*l-1)//6)
    print((ans1-ans2%1000000007))

# Method 3 (Don't repeat with squaring)
for _ in range(int(input())):
    l,r = map(int,input().split())
    ans1 = (r*(r+1)//2 - l*(l-1)//2)**2
    ans2 = (r*(r+1)*(2*r+1)//6) - (l*(l-1)*(2*l-1)//6)
    print((ans1-ans2%1000000007))
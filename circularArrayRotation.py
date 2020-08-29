# First Solution

n,k,q = map(int,input().split())
n1 = list(map(int,input().split()))
q1 = [int(input()) for x in range(q)]

p = n1[k-1:] + n1[:-k]
for x in q1:
    print(p[x])

# Second Solution

length, ops, qs = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

delta = ops % length

for _ in range(qs):
    index = int(input())
    print(nums[index - delta])
    


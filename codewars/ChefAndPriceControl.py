# cook your dish here
for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    l1 = [x if x<k else k for x in l]
    print(sum(l)-sum(l1))
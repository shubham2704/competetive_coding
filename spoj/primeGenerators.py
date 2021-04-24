import math

for _ in range(int(input())):

    n,m = map(int,input().split())
    for num in range(n,m):
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
            print (num)
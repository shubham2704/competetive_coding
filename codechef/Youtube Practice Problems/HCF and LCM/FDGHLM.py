import math

a,b = map(int,input().split())
print(math.gcd(a,b), (a*b)//math.gcd(a,b))
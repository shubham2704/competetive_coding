import math

w,s = map(float,input().split())
si = math.sin(s)
ta = w/si
print(round(ta,2))
print(si)
print(ta)
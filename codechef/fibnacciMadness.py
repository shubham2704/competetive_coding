import math

n = int(input())
fi = 1.618034
x = (fi**n - (1-fi)**n)/math.sqrt(5)
print(math.floor(x))
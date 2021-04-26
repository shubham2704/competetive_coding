import sys
from math import floor

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = floor(n**0.5)
    print(*[x*x for x in range(1,a+1)])
    # Need to print the perfect square between the range [1,n](inclusive)
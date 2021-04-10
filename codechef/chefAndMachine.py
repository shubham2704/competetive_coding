# Calculates the Factorial of a given number
import itertools as it
import operator as op

def factorials_nums(n):
    result = list(it.accumulate(it.chain([1], range(1, 1 + n)), op.mul))
    return result[-1]

for _ in range(int(input())):
    x = int(input())
    print(factorials_nums(x))

# By Recusrion
def fact(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return n*fact(n-1)

print(fact(2000))
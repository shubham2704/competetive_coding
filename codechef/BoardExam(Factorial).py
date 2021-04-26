import itertools as it
import operator as op

def factorials_nums(n):
    result = list(it.accumulate(it.chain([1], range(1, 1 + n)), op.mul))
    return result[-1]

for _ in range(int(input())):
    n,x,y = map(int,input().split())
    fact_N = factorials_nums(n)
    fact_X = factorials_nums(x)
    fact_Y = factorials_nums(y)
    fact_NX = factorials_nums(n-x)
    fact_NY = factorials_nums(n-y)

    print((fact_N//(fact_X * fact_NX)) * (fact_N//(fact_Y * fact_NY)))

    # res = (fact_N//(fact_X * fact_NX)) * (fact_N//(fact_Y * fact_NY)) 
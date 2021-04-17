import itertools as it
import operator as op

def factorials_nums(n):
    result = list(it.accumulate(it.chain([1], range(1, 1 + n)), op.mul))
    return result[-1]
f = factorials_nums(60)
a = str(f).rstrip('0')
print(len(str(f)) - len(a))
print(factorials_nums(60))
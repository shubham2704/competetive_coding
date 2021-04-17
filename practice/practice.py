import itertools as it
import operator as op

def factorials_nums(n):
    result = list(it.accumulate(it.chain([1], range(1, 1 + n)), op.mul))
    return result[-1]
f = str(factorials_nums(60))
a = f.rstrip('0')
print(len(f) - len(a))
print(factorials_nums(60))
b = f.count('5')
print(b)
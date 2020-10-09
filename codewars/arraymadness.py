def array_madness(a,b):
    return sum(x**2 for x in a)> sum(y**3 for y in b)
print(array_madness([4, 5, 6], [1, 2, 3]))
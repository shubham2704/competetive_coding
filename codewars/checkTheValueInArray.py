def check(seq, elem):
    return True if elem in seq else False
print(check([1,2,3],4))

# Better way
def check1(s,e):
    return e in s
print(check1([1,2,3],3))
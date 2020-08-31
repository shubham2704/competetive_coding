# First Solution
def array_diff(a, b):
    res = [i for i in a if i not in b]
    return res
print(array_diff([1,2,2,2,3],[2]))



# First Solution
def array_diff_1(a, b):
    return [x for x in a if x not in b]
print(array_diff_1([1,2,2,2,3],[2]))
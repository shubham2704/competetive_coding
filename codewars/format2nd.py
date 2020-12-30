def print_nums(*arr):
    if not arr: return ''
    ln = len(str(max(arr)))
    return '\n'.join(str(c).zfill(ln) for c in arr)

print(print_nums(1, 23, 2, 17, 102 ))
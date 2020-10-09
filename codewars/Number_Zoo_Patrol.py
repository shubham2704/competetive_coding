def find_missing_number(n):
    a = len(n)+1
    return a*(a+1)/2 - sum(n)

print(find_missing_number([4, 2, 3]))
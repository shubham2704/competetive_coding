def check_power(a,n):
    return -1 if len(a)<n else a[n]**n

print(check_power([1, 2, 3, 4], 2))
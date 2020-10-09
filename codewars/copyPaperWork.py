def paperwork(n, m):
    return sum([0 if n<0 or m<0 else abs(n*m)])
print(paperwork(5,5))
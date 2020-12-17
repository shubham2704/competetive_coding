def pascals_triangle(n):
    
    def fact(n):
        f = 1
        i = 1
        while i<=n:
            f = f*i
            i+=1
        return f
    
    lines = n
    m = []
    for x in range(lines):
        for y in range(x+1):
            y = fact(x)//(fact(y)*fact(x-y))
            m.append(y)
            y = 0
    return m

print(pascals_triangle(4))
print(pascals_triangle(12))
print(pascals_triangle(6))

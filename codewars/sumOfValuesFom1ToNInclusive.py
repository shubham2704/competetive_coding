# Naive Method
def total1(n):
    s = 0
    for i in range(n+1):
        s+=i
    return s
print(total1(10))

# List Comperhension
def total2(n):
    return sum(x for x in range(n+1))
print(total2(20))

# Pro Method 
def total(n):
    return (n*(n+1)//2)
print(total(34))
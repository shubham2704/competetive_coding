# Method one
def divisors(n):
    if n == 1:
        return "{} is prime".format(n)
    else:
        c = [x for x in range(2,n//2+1) if n%x==0]
        if len(c)==0:
            return "{} is prime".format(n)
        else:
            return c
print(divisors(12))
print(divisors(25))
print(divisors(13))
print("------------------------------------------------")

# Method Two
def divisors_1(n):
    c = [x for x in range(2,n//2+1) if n%x==0]
    if len(c)==0:
        return f'{n} is prime'
    else:
        return c
print(divisors_1(12))
print(divisors_1(25))
print(divisors_1(13))
print("------------------------------------------------")

# Shorthand for Method Two
def divisors_2(n):return f'{n} is prime' if len([x for x in range(2,n//2+1) if n%x==0]) == 0 else [x for x in range(2,n//2+1) if n%x==0]

print(divisors_2(12))
print(divisors_2(25))
print(divisors_2(13))
print("------------------------------------------------")

# Implementeing wiht Lambda Functions
divisors_3 = lambda n: f'{n} is prime' if len([x for x in range(2,n//2+1) if n%x==0]) == 0 else [x for x in range(2,n//2+1) if n%x==0]

print(divisors_3(12))
print(divisors_3(25))
print(divisors_3(13))
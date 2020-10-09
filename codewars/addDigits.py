# Method One
def get_sum_of_digits(num):
    l = list(str(num))
    return sum(int(x) for x in l)

print(get_sum_of_digits(123))

# Method Two // One Liner
def get_sum_of_digits_better(num):
    return sum(int(x) for x in str(num))

print(get_sum_of_digits_better(123))
#Basic
def high_and_low(numbers):
    # ...
    l = list(map(int,numbers.split()))
    a = max(l)
    b = min(l)
    l1 = [str(a),str(b)]
    return " ".join(l1)
print(high_and_low("1 2 -3 4 5"))

#Advanced
def high_and_low_1(n): return " ".join([max(n.split()),min(n.split())])
print(high_and_low_1("1 2 -3 4 5"))
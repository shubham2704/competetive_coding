# from functools import reduce
# from math import sqrt
# from itertools import count, islice

# def is_prime(n):
#     return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

# if is_prime(3):
#     print('yes')
# else:
#     print('No')

# def factors(n):
#     return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
# l = factors(100)
# c = 0
# for i in l:
#     if i>=1:
#         c+=1 

# print(list(range(1,6)))
# print(c)
# print(l)

from functools import reduce
from math import sqrt
from itertools import count,islice

def strange_sum (L, R):
    l = list(range(L,R+1))
    res = []
    res1 = []
    for i in l:
        def factors(n):
            return sorted(set(reduce(list.__add__,([i,n//i] for i in range(1,int(n**0.5+1))if n%i==0))))
        fact = factors(i)
        
        for x in fact:
            if x==1:
                res1.append(0)
            elif x>1:
                def is_prime(n):
                    return n>1 and all(n%i for i in islice(count(2),int(sqrt(n)-1)))
                if is_prime(x):
                    res1.append(1)
            else:
                x = 0
                y = 0
                for z in fact:
                    temp = i//z
                    if temp>=z and temp*z==i:
                        x = z
                        y = temp
                
                res1.append(x*y)
                res1.append(y*x)
        s = sum(res1)
        res.append(s)
        res1 = []
    return sum


    

T = int(input())
for _ in range(T):
    L = int(input())
    R = int(input())

    out_ = strange_sum(L, R)
    print (out_)
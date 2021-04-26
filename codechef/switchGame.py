for _ in range(int(input())):
    n = int(input())
    res = '1 '
    for x in range(2,n+1):
        if x%2==0 or x%3==0 or x%4==0 or x%5==0 or x%6==0 or x%7==0 or x%8==0 or x%9==0 or x%10==0:
            pass
        else:
            res += str(x) + ' '
    print(res)

# MAX = 100
# is_prime = [True for _ in range(MAX)]
# is_prime[0] = is_prime[1] = False
# for i in range(2, int(MAX ** (1 / 2)) + 1):
#   if is_prime[i]:
#     for j in range(i ** 2, MAX, i):
#       is_prime[j] = False 
# primes = [i for i in range(MAX) if is_prime[i]] 
# n = 1
# print(primes)
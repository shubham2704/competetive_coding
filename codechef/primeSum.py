MAX = 105000

is_prime = [True for _ in range(MAX)]
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX ** (1 / 2)) + 1):
  if is_prime[i]:
    for j in range(i ** 2, MAX, i):
      is_prime[j] = False 
primes = [i for i in range(MAX) if is_prime[i]] 

n = int(input())
print(sum(primes[:n]))
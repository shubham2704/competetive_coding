# Naive Solution

n = 942
sum = 0
while n>0 or sum >9:
    if n==0:
        n=sum
        sum=0
    sum+=n%10
    n//=10
print(sum)

# One Liner

n = 493193 
print(n if n<10 else n%9)
print(n%9 or n and 9)
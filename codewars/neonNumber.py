num = int(input('Enter the number : '))

sq = num*num
sum = 0

while sq>0:
    sum = sum + sq%10
    sq = sq//10

if sum == num:
    print(f'{num} is Neon Number.')
else:
    print(f'{num} is Not Neon Number.')

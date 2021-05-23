from itertools import product

for x in range(int(input())):
    l = 'abcdefghijklmnopqrstuvwxyz'
    n,k = map(int,input().split())
    s = input()
    alpha = l[:k]
    keywords = [''.join(i) for i in product(alpha, repeat=n)]
    till = keywords.index(s)
    new_l = keywords[:till]
    res = sum(1 if x==x[::-1] else 0 for x in new_l)

    print(f'Case #{x+1}: {res}')
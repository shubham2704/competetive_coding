def beeramid(bonus, price):
    # your code
    beers = bonus//price
    c = 0
    for i in range(1,101):
        c = (i*(i+1)*(2*i+1))/6
        
        if c == beers:
            return i
        elif c> beers:
            return i-1
print(beeramid(5000,3))
print(beeramid(1500, 2))
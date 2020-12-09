def hydrate(d): 
    res = sum(int(x) for x in d.split() if x.isdigit())
    return f'{res} glasses of water' if res>1 else f'{res} glass of water'

print(hydrate("1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"))
t = int(input())

while t:
    
    n = input()
    x = 0
    
    for i in n:
        if i is '1':
            x = x+1
    
    if x%2 == 0:
        print("LOSE")
    else:
        print("WIN")
    
    t=t-1
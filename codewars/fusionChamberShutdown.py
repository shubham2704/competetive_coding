def burner(c,h,o):
    water = co2 = methane = 0
    
    while h > 1 and o > 0:
        water += 1
        h -= 2
        o -= 1
    
    while c > 0 and o > 1:
        co2 += 1
        c -= 1
        o -= 2
        
    while c > 0 and h > 3:
        methane += 1
        c -= 1
        h -= 4
        
    return water,co2,methane

print(burner(5,45,0))
print(burner(45,11,100))
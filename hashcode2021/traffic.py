# file = open("a.txt", 'r')
# data = file.read()

# line1 = file.readline().split()
# print(line1)

# # print (data)

# file.close() 

with open("a.txt", 'r') as file:
    line1 = file.readline().split()
    d = int(line1[0])
    i = int(line1[1])
    s = int(line1[2])
    v= int(line1[3])

    print(line1)
    print()
    street_names = []
    lines = file.readlines()

    for line in lines[:s]:
        strip = line.strip().split()
        street_names.append(strip[2])
        print(strip)
    
    print()
    print(street_names)
        
    

    for cars in lines[s:]:
        cars_ = cars.strip()
        # print(cars_)

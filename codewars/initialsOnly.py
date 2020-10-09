def abbrevName(name):
    return ".".join(x[0].upper() for x in name.split(" ") )
print(abbrevName("shubham goswami"))
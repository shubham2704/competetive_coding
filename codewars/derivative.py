def derive(c, e): 
    s = str(c*e)
    return "{}x^{}".format(s,e-1)

print(derive(7,8))
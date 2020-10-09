def getTheMiddleChar(s):
    return s[len(s)//2-1]+s[len(s)//2] if len(s)%2==0 else s[len(s)//2]
print(getTheMiddleChar('testing'))

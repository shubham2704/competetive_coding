def create_phone_number(n):
    #your code here
    s = ''
    for i in n:
        s+=str(i)
    
    t = "(" + s[:3]+")" + " " +s[3:6] + "-" + s[6:]
    return t
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number(list(map(int,input().split()))))
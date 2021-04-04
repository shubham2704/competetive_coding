# for x in range(int(input())):
#     s = input().split()
#     x,y,st = s[0], s[1], [x for x in s[2]]


    
def moons(p,x,y):
    fees = 0
    fees =p.count("CJ")*x + p.count("JC")*y
    return fees

def solve():
    t= input().split()
    x = int(t[0])
    y = int(t[1])
    p = t[2]

    fees = moons(p,x,y)
    length = len(p)
    i = 0

    while i < length:
        m =""
        if i > 0 and p[i] == "?":
            m = p[i-1]

        while p[i] == "?":
            if i < (length-1):
                i = i+1
            else:
                break

        f = m + p[i]
        if f == "CJ":
                fees += x
        elif f == "JC":
                fees += y
        i+=1

    print("Case #"+str(z+1)+": "+ str(fees))

for z in range(int(input())):
    solve()
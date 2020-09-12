
def points(games):
    p = 0
    for x in games:
        x1,y1  = int(x[0]),int(x[-1]) 
        if x1>y1:
            p+=3
        elif x1==y1:
            p+=1
        else:
            pass
    return p
print(points(["3:1", "2:2", "0:1"]))

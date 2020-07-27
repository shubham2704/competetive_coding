def pig_it(text):
    #your code here
    l = list(map(str,(text).split(" ")))
    pun = ["!","?",","]
    b = ""
    m = []
    for i in l:
        if i in pun:
            m.append(i)
        else:
            b = i[1:] + i[:1] + "ay"
            m.append(b)
    return " ".join(m)

print(pig_it('Hello world !'))
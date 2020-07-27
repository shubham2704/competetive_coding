# Naive Method
def pig_it(text):
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

# Pro Version
def pig_it1(text):
    l = list(map(str,text.split(" ")))
    pun = ['!','?',',']
    return " ".join(x if x in pun else x[1:]+x[:1]+'ay' for x in l)
print(pig_it1('Pig latin is cool'))

# Pro version 2

def pig_it2(text):
    return " ".join(x[1:]+x[:1]+'ay' if x.isalpha() else x for x in text.split(" "))

print(pig_it2('Pig latin is cool'))
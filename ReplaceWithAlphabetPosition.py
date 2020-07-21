def alphabet_position(text):
    t = list(text.upper())
    m = [ord(i)-ord('@') for i in t if i.isalpha()]       
    return " ".join([str(e) for e in m])

print(alphabet_position("The sunset sets at twelve o' clock."))
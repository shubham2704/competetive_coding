# Method 1
def meeting(s):
    return ''.join(sorted('({1}, {0})'.format(*(x.split(':'))) for x in s.upper().split(';')))
print(meeting("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))

# Method 2
def meeting1(s):

    s = s.upper()
    s = s.split(';')
    array = []
    string = ""

    for i in s:
        i = i.split(':')
        string = '('+i[1]+', '+i[0]+')'
        array.append(string)
    
    array.sort()
    output = ""
    
    for j in array:
        output += j
    
    return output
print(meeting1("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))
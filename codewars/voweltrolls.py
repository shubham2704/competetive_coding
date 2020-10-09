s = 'This website is for losers LOL!'
def vowelTrolls(s):
    s.split(' ')
    s1 =''
    for x in s:
        for y in x:
            if y.lower() not in ['a','e','i','o','u']:
                s1+=y
    return(s1)
print(vowelTrolls(s))
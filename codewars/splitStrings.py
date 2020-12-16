def solution(s):
    l = []
    m = ''
    for x in range(0,len(s)-1,2):
        m = s[x]+s[x+1]
        l.append(m)
        m = ''
    if len(s)%2==0:
        return l
    else:
        l.append(s[-1]+'_')
        return l

print(solution('abc'))
print(solution('abcd'))
print(solution('abcde'))
print(solution('abcdef'))
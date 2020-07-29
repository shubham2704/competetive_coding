s = input().lower()
for i in s:
    if i in ['a','s','m','d']:
        a = int(s[:s.index(i)])
        b = int(s[s.index(i)+1:])

        if i == 'a':
            print(int(a+b))
        elif i == 's':
            print(int(a-b))
        elif i == 'm':
            print(int(a*b))
        else:
            print(int(a/b))

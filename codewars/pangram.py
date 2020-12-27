def is_pangram(s):
    c = 'abcdefghijklmnopqrstuvwxyz'
    for x in c:
        if x not in s.lower():
            return False
    return True

print(is_pangram('Hello World !'))
print(is_pangram('The quick brown fox jumps over the lazy dog'))
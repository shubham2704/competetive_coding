def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

print(longest("xyaabbbccccdefww", "abcdefklmopqwxy"))
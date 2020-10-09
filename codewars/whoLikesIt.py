def whoLikesIt(s):
    if len(s)==0:
        return "no one likes this"
    elif len(s)==1:
        return f'{s[0]} likes this'
    elif len(s)==2:
        return f'{s[0]} and {s[1]} likes this'
    elif len(s)==3:
        return f'{s[0]}, {s[1]} and {s[2]} likes this'
    else:
        return f'{s[0]}, {s[1]} and {len(s)-2} others likes this'

print(whoLikesIt([]))
print(whoLikesIt(["Peter"]))
print(whoLikesIt(["Jacob", "Alex"]))
print(whoLikesIt(["Max", "John", "Mark"]))
print(whoLikesIt(["Alex", "Jacob", "Mark", "Max"]))
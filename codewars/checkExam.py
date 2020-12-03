# Method 1
def check_exam(a1,a2):
    res = 0
    for x,y in zip(a1,a2):
        if x == y :
            res +=4
        elif y == "":
            pass
        elif x != y:
            res -= 1
            
    return res if res > 0 else 0

print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))

# Method 2

def check_exam2(a1,a2):
    return max(0, sum(4 if a == b else -1 for a, b in zip(a1, a2) if b))

print(check_exam2(["a", "a", "b", "b"], ["a", "c", "b", "d"]))
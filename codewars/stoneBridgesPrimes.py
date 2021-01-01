def isPrime(x):
    if x <= 3: # ignore cases of 0 and 1
        return True
    f = 2
    while f * f <= x:
        if x % f == 0:
            return False
        f += 2 if f != 2 else 1
    return True

def solve(x, y):
    answer = 0
    for m in range(21): # 2^21 > 1.5M
        for n in range(13): # 3^13 > 1.5M
            suspect = 2 ** m * 3 ** n + 1
            if suspect > y:
                continue
            if x <= suspect < y and isPrime(suspect):
                answer += 1
    return answer
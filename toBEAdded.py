"""
Find Divisors

Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"

Solution

def divisors(n):
    if n == 1:
        return "{} is prime".format(n)
    else:
        c = [x for x in range(2,n//2+1) if n%x==0]
        if len(c)==0:
            return "{} is prime".format(n)
        else:
            return c
"""


"""
Beeramid


Let's pretend your company just hired your friend from college and paid you a referral bonus. Awesome! To celebrate, you're taking your team out to the terrible dive bar next door and using the referral bonus to buy, and build, the largest three-dimensional beer can pyramid you can. And then probably drink those beers, because let's pretend it's Friday too.

A beer can pyramid will square the number of cans in each level - 1 can in the top level, 4 in the second, 9 in the next, 16, 25...

Complete the beeramid function to return the number of complete levels of a beer can pyramid you can make, given the parameters of:

1) your referral bonus, and

2) the price of a beer can

For example:

beeramid(1500, 2); // should === 12
beeramid(5000, 3); // should === 16


Solution


def beeramid(bonus, price):
    # your code
    beers = bonus//price
    c = 0
    for i in range(1,101):
        c = (i*(i+1)*(2*i+1))/6
        
        if c == beers:
            return i
        elif c> beers:
            return i-1
"""
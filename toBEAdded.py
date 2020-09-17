"""
Beginner Series #1 School Paperwork

Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need.


Solution

def paperwork(n, m):
    return sum([0 if n<0 or m<0 else abs(n*m)])
"""


"""

You only need one - Beginner


You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either.

Return true if the array contains the value, false if not.

Solution

def check(seq, elem):
    return True if elem in seq else False
"""

"""
Speed code Array Madness


Given two integer arrays a, b, both of length >= 1, create a program that returns true if the sum of the squares of each element in a is strictly greater than the sum of the cubes of each element in b.

E.g.

array_madness([4, 5, 6], [1, 2, 3]) => True #because 4 ** 2 + 5 ** 2 + 6 ** 2 > 1 ** 3 + 2 ** 3 + 3 ** 3


Solution

def array_madness(a,b):
    return sum(x**2 for x in a)> sum(y**3 for y in b)
"""

"""
All star coding challenge

This Kata is intended as a small challenge for my students

All Star Code Challenge #18

Create a function called that accepts 2 string arguments and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

strCount('Hello', 'o') // => 1
strCount('Hello', 'l') // => 2
strCount('', 'z')      // => 0

Solution

def str_count(s, l):
    # Your code here ;)
    c =0
    for i in s:
        if l==i:
            c+=1
    return c
"""

"""
Is it Even

In this Kata we are passing a number (n) into a function.

Your code will determine if the number passed is even (or not).

The function needs to return either a true or false.

Numbers may be positive or negative, integers or floats.

Floats are considered UNeven for this kata.


Solution

def is_even(n): 
    # your code here
    return True if n%2==0 else False
"""

"""
Sum of Digits


Debug   function getSumOfDigits that takes positive integer to calculate sum of it's digits. Assume that argument is an integer.

Example
123  => 6
223  => 7
1337 => 15

Solution

def get_sum_of_digits(num):
    l = list(str(num))
    return sum(int(x) for x in l)
"""


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
"""
Binary Addition

Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.


Solution

def add_binary(a,b):
    #your code here
    n = a+b
    b = bin(n).replace("0b","")
    
    return str(b)

"""


"""
Highest And Lowest

In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

Solution

def high_and_low(numbers):
    # ...
    l = list(map(int,numbers.split()))
    a = max(l)
    b = min(l)
    l1 = [str(a),str(b)]
    return " ".join(l1)

"""


"""
Sorted Odd


You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]


Solution

def sort_array(source_array):
    # Return a sorted array.
    o = iter(sorted(e for e in source_array if e%2))    
    return [next(o) if e%2 else e for e in source_array]

"""


"""

The Amount of Points


Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.

For example: ["3:1", "2:2", "0:1", ...]

Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:

if x>y - 3 points
if x<y - 0 point
if x=y - 1 point
Notes:

there are 10 matches in the championship
0 <= x <= 4
0 <= y <= 4


Solution

def points(games):
    p = 0
    for x in games:
        x1,y1  = int(x[0]),int(x[-1]) 
        if x1>y1:
            p+=3
        elif x1==y1:
            p+=1
        else:
            pass
    return p
"""


"""
Camel case Method

Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.

For instance:

camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord

Solution

def camel_case(string):
    return "".join(x for x in string.title() if not x.isspace())

"""

"""

Abbreviate a Two Word Name

Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F


Solution

def abbrevName(name):
    return ".".join(x[0].upper() for x in name.split(" ") )
"""


"""

Array Plus Array

I'm new to coding and now I want to get the sum of two arrays...actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too.


Solution

def array_plus_array(arr1,arr2):
    return sum(arr1)+sum(arr2)
"""


"""
Beginner Series #1 School Paperwork

Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need.


Solution

def paperwork(n, m):
    # Happy Coding! ^_^
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
Is String Upper Case

Create a method is_uppercase() to see whether the string is ALL CAPS. For example:

is_uppercase("c") == False
is_uppercase("C") == True
is_uppercase("hello I AM DONALD") == False
is_uppercase("HELLO I AM DONALD") == True
is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ") == False
is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ") == True

Solution

def is_uppercase(inp):
    return True if inp.isupper() else False
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
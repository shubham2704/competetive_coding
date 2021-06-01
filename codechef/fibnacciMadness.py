# Finding nth finbacci with math formulae  module
import math

n = int(input())
fi = 1.618034
x = (fi**n - (1-fi)**n)/math.sqrt(5)
print(math.floor(x))

import math

m = int(input())
n = float(m)
fi = 1.618034
try:
    x = (fi**(n-1) - (1-fi)**(n-1))/math.sqrt(5)
    print(math.floor(x))
    print('Alive' if math.floor(x)%2!=0 else 'Dead')
except:
    print('overflow')


# Finding nth fibonacci with  bitwise operator much efficient
def findNature(a, b, n):
	if (n == 0):
		return (a & 1);

	if (n == 1):
		return (b & 1);

	
	if ((a & 1) == 0):
		
		if ((b & 1) == 0):
			return False;
		
		else:
			return True if(n % 3 != 0) else False;

	else:
		
		if ((b & 1) == 0):
			return True if((n - 1) % 3 != 0) else False;
		
		else:
			return True if((n + 1) % 3 != 0) else False;

a = 0;
b = 1;
n = int(input())

if (findNature(a, b, (n-1)) == True):
	print("Alive", end = " ");
else:
	print("Dead", end = " ");


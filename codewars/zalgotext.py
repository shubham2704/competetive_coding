# Method 1 BEST
def read_zalgo(zalgotext):
    return "".join([c for c in zalgotext if c.isascii()])
print(read_zalgo())

# Method 2 Regex
import re

def read_zalgo(s):
    return re.sub('[^\w .,!?]','',s)
print()


# Method 1
import math

cockroach_speed = lambda s : math.floor(s * 27.777778)

print(cockroach_speed(1.08))

# Method 2
import math
def cockroach_speed2(S): return math.floor(S * 27.777778)

print(cockroach_speed2(1.08))

# Method 3 without math.floor()
def cockroach_speed3(s): return s // 0.036

print(cockroach_speed3(1.08))
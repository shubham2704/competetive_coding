# import math
# from itertools import permutations
# class permute:

#     n = 0
#     count = 0

#     def __init__(self, n):
#         self.n = n

#     def next(self):
#         a = []
#         num = self.count
#         for i in range(self.n-1, 0, -1):
#             f = math.factorial(i)
#             c = math.floor(num / f)
#             a.append(c+1)
#             num = num - c*f
#         self.count = self.count+1
#         a.append(1)
#         return self.fill(a)

#     def fill(self, a):
#         p = [0]*self.n
#         v = self.n
#         for i in range(0, len(a)):
#             zeroes = 0
#             for j in range(0, len(p)):
#                 if p[j] == 0:
#                     zeroes +=1
#                 if zeroes == a[i]:
#                     p[j] = v
#                     v -= 1
#                     break
#         return p
        
# def genlist(l,n1,c1):
#     n2 = math.factorial(n1)
#     p = permute(n1)
#     for o in range(n2):
#         ln = p.next()
#         lnc = ln[0:]
#         c = 0
#         for i in range(n1-1):
            
#             j = ln.index(min(ln[i:n1+1]))
#             ln[i:j + 1] = reversed(ln[i:j + 1])
        
#             c += (j)-(i)+1
            
#         if c1 == c:
#             return lnc
#     return -1

# n = int(input())
# lf = []
# for k in range(n):
#     l = input()
#     l = l.split()
#     n1 = int(l[0])
#     c1 = int(l[1])
#     l = []

#     for i in range(1,n1+1):
#         l.append(i)

#     ln = genlist(l,n1,c1)

#     if ln == -1:
#         lf.append('IMPOSSIBLE')
#     else:
#         s = [str(i) for i in ln]
#         st = " ".join(s)
#         lf.append(st)

# for i in range(n):
#     print('Case #'+str(i+1)+": "+lf[i])

def createL(n):
    l = []
    for i in range(1,n+1):
        l.append(i)
    return l 

def operationL(n, p):
    if p < n-1:
        return []
    l = []
    t = 0 
    c = 1
    for i in range(n-1, 0, -1):
        c += 1

        if t+c+i-1 >= p:
            r = p-t-i+1
            l.append(r)
            for k in range(i-1):
                l.append(1)
            t = p
            break

        t += c 
        l.append(c)
    if t<p:
        return []
    return l

def operate(l, opeL):
    length = len(opeL)
    for i in range(length):
        t = len(l)-(i+2)
        sp = t+opeL[i]
        l = l[:t]+ list(reversed(l[t:sp])) + l[sp:]
    return l 

def solve():
    inp = input().split()
    n = int(inp[0])
    p = int(inp[1])
    l = createL(n)
    opeL = operationL(n,p)
    l = operate(l, opeL)
    result = " "
    if opeL:
        for item in l:
            result += str(item)+ " "
    else:
        result =" IMPOSSIBLE"
    print("Case #"+str(i+1)+": "+ str(result))

for i in range(int(input())):
    solve()
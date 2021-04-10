# # Other Code
# testCases = int(input())
# def check(nxt, curr, count = 0):
#     def hit():
#         nonlocal count
#         for ir in range(1, 10):
#             strn = int(str(nxt) + str(ir))
#             if strn > curr:
#                 count += 1
#                 return strn

#             if ir == 9:
#                 count +=1
#                 return strn

#     test = hit()
#     if test <= curr:
#         return check(test, curr, count=count)
#     return count, test

# for i in range(testCases):
#     count = int(input())
#     numbers = [int(number) for number in input().split()]
#     list_len = len(numbers)
#     changes = 0

#     for index, item in enumerate(numbers):
#         try:
#             nextValue = numbers[index + 1]
#             if item >= nextValue:
#                 e = check(nextValue, item)
#                 changes += e[0]
#                 numbers[index + 1] = e[1]
#         except:
#             pass        
#     print(f'Case #{i+1}: {changes}')


# # My Code
# for t in range(int(input())):
#     n = int(input())
#     l = list(map(int,input().split()))
#     l1 = sorted(l)
#     l2 = set(l)
#     flag = 0
#     if len(l2)==1:
#         print(f'case #{t+1}: 1')
#     elif l1 == l:
#         print(f'case #{t+1}: 0')
#     else:
#         for x in range(n-1):
#             while l[x]>=l[x+1] :
#                 l[x+1] = l[x+1]*10 + 9
#                 flag+=1
#         print(f'case #{t+1}: {flag}')
#         print(l)

def getAnswer(n,lst):
    count=0
    for i in range(1,n):
        if lst[i]<lst[i-1]:
            cur=str(lst[i])
            prev=str(lst[i-1])
            d=len(cur)-len(prev)
            for j in range(d):
                cur.append("0")
                count+=1
            cur=int(cur)
            prev=int(prev)
            if cur>prev:
                lst[i]=cur
            else:
                for k in range(9):
                    cur+=1
                    if cur>prev:
                        break
                if cur<prev:
                    cur=str(cur)
                    cur.append("0")
                    count+=1
                    lst[i]=int(cur)
    return count            
                
t=int(input())
for i in range(t):
    n=int(input())
    lst=[]
    for j in range(n):
        lst.append(int(input()))
    strg="Case #"
    strg.append(str(i))
    strg.append(":")
    print(strg,getAnswer(n,lst))
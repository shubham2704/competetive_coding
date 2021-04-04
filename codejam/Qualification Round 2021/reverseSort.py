for x in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))

    cost = 0
    for i in range(n-1):
        j = l.index(min(l[i:n]))
        l[i:j+1] = reversed(l[i:j+1])
        cost += (j-i) +1
    print(f'Case #{x+1}: {cost}')

# for x in range(int(input())):
#     n = int(input())
#     l = list(map(int,input().split()))

#     m = 0
#     cost = 0
#     costlist = []
#     s = []

#     for i in range(len(l)-1):
#         m = l.index(min(l))
#         l1 = l[i:m+1]
#         j = l1.index(min(l1))

#         cost = (j-i)+1
#         costlist.append(cost)
#         m = 0
#         l1 = []
#         s.append(j)
#         s.append(i)
#         s.sort()
#         if len(s) == len(l):
#             break
    
#     if l == [4,2,1,3]:
#         print(f'Case #{x+1}: 6')
#     else:
#         print(f'Case #{x+1}: {sum(costlist)}')
#     s = []
#     costlist = []
    

# reverse = int(input())  
# for i in range(1, reverse + 1):
#     a = int(input())
#     b = list(map(int, input().split()))
#     out = 0
#     for index in range(a-1):
#         min_index = b.index(min(b[index:a]))
#         b[index: min_index + 1] = reversed(b[index: min_index + 1])
#         out += (min_index) - (index) + 1
#     print("Case #{}: {}".format(i, out))


# for _ in range(int(input())):
#     s = input()
#     print(len(' '.join(s.split('0')).split()))

i = 0
s = []
l = [7,6,5,4,3,2,1]
print(l.index(min(l)))
l1 = l[i:l.index(min(l))+1]
j = l1.index(min(l1))
s.append(l[j])
s.append(l[i])
print(s)
j = 0
c1 = []
for i in range(6):
    c = i+j
    c1.append(c)
    j+=1
    print(f'{i} + {j} = {c}')
print(c1)
print(sum(c1))
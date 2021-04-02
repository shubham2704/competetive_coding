def accenture(N, V):
    count = 0
    itr = V
    index = 0
    for item in itr:
        ints = int(item)
        try:
            nextSpeed = int(itr[index + 1])
            if ints > nextSpeed:
                itr[index + 1] = ints + 1
                count+= 1
        except Exception as e:
            pass
        index +=1
    return count

for _ in range(int(input())):
    n = int(input())
    v = list(map(int,input().split()))
    print(accenture(n,v))
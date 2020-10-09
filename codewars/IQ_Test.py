def iq_test(n):
    n1 = list(map(int, n.split()))
    even = [int(x) for x in n1 if x%2==0]
    odd = [int(x) for x in n1 if x%2!=0]
    
    return n1.index(even[0])+1 if len(even)==1 else n1.index(odd[0])+1

n = input()
print(iq_test(n))
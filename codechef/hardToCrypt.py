# Basic Method
n = int(input())
arr = list(map(int,input().strip().split()))
c = 0
for i in range(0,len(arr)-3):
    for j in range(i+1,len(arr)-2):
        for k in range(j+1,len(arr)-1):
            for l in range(k+1,len(arr)):
                if(arr[l]-arr[k] == arr[k]-arr[j] and arr[k]-arr[j] == arr[j]-arr[i] and arr[l]-arr[k] == arr[j]-arr[i]):
                    c+=1
print(c)

# Advanced Method
from itertools import combinations
c=0
n=int(input())
l=list(map(int,input().split()))
for i in list(combinations(l,4)):
    if(i[1]-i[0]==i[2]-i[1]==i[3]-i[2] and (i[0]<=i[1]<=i[2]<=i[3] or i[0]>=i[1]>=i[2]>=i[3] )):
        c+=1
print(c)


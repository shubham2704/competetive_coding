# for _ in range(int(input())):
#     n,m,k = map(int,input().split())
#     matrix = []
#     for i in range(n):
#         l = list(map(int,input().split()))
#         matrix.append(l)
#         l = []
#     print(matrix)

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
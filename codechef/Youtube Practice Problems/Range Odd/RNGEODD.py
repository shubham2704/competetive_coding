l,r = map(int,input().split())
print(' '.join(str(x) for x in range(l,r+1) if x%2!=0))
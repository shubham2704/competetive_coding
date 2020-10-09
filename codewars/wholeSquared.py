m = int(input())
i = list(map(int,input().split()))
c = 1
l = []
while 1:
	if c**2 > m:
		break
	else:
		if c**2 not in i:
			l.append(c**2)
	c+=1
print(l)
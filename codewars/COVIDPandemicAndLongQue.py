# cook your dish here
t = int(input())

for _ in range(t):
	n = int(input())
	z = list(map(int,input().split()))
	c = []
	for i,j in enumerate(z):
		if j == 1:
			c.append(i)

	res = [c[i + 1] - c[i] for i in range(len(c)-1)] 
	s = 0
	for k in res:
		if k<6:
			s+=1
		else:
			pass

	if s >0:
		print("NO")
	else:
		print("YES")
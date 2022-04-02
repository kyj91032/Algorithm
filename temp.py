a, b, c = map(int, input().split())

i = 0
while 1:
	y1 = a + 15 * i
	y2 = (y1 - b) / 28
	if y2 % 1 == 0 and y2 > 0:
		y3 = (y2 - c) / 19
		if y3 % 1 == 0 and y3 > 0:
			print(int(y3))
			break
		else:
			i += 1
	else:
		i += 1


T = int(input())


for i in range(1, T + 1):
	print("Case #%d: " % i, end = '')
	
	n = int(input())
	
	graph = [0]
	
	fl = list(map(int, input().split()))
	pl = list(map(int, input().split()))
	
	for j in range(1, n + 1):
		graph.append((pl[i - 1], fl[i - 1]))
	
	visited = [False] * (n + 1)
	
	itr = []
	for j in range(n + 1):
		if j not in pl:
			itr.append(j)
	
	sum = []
	
	tmp = 0
	
	def dfs(v):
		visited[v] = True
		
		if v not in pl:
			sum.append(tmp)
		for k in range(n):
			if pl[k] == v:
				if not visited[k + 1]:
					dfs(k + 1)
		
	

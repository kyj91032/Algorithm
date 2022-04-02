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

def dfs(v):
	global tmp
	global sl
	if not visited[v]:
		visited[v] = True
		tmp += fi[v - 1]
		for i in graph[v]:
			dfs(i)
	sl.append((tmp, v))
	tmp -= fi[v - 1]

def dfs2(v):
	global m
	if v == 0:
		return
	if visited2[v] == True:
		return
	visited2[v] = True
	m = max(m, fi[v - 1])
	dfs2(pi[v - 1])

for i in range(1, T + 1):
	print("Case #%d: " % i, end = '')
	
	n = int(input())
	
	fi = list(map(int, input().split()))
	pi = list(map(int, input().split()))
	
	graph = [[] for _ in range(n + 1)]
	
	visited = [False] * (n + 1)
	visited2 = [False] * (n + 1)
	
	for a in range(n + 1):
		for b in range(n):
			if pi[b] == a:
				graph[a].append(b + 1)
	
	tmp = 0
	sl = []
	
	ini = []
	for j in range(n + 1):
		if len(graph[j]) == 0:
			ini.append(j)
	
	p0 = []
	for j in range(n):
		if pi[j] == 0:
			p0.append(j + 1)
	
	result = 0
	
	for q in p0:
		
		dfs(q)

		isl = []
		l = len(sl)
		for j in range(l):
			if sl[j][1] in ini:
				isl.append(sl[j])
		
		isls = sorted(isl, key = lambda x : x[0])
		
		islsi = []
		for j in range(len(isls)):
			islsi.append(isls[j][1])	

		m = 0
		M = 0
	
		for u in islsi:
			m = 0
			dfs2(u)
			M += m
	
		result += M
		
	print(result)

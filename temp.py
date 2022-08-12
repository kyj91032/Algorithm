import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())

a = []

for i in range(n):
	for j in range(m):
		a.append(list(map(int, input().split())))

r = list(map(int, input().split()))

for i in r:
	if r == 1:
		a.reverse()
	if r == 2:
		for j in range(n):
			a[j].reverse()
	if r == 3:
		tmp = [[] for _ in range(m)]
		for j in range(m):
			for k in range(n):
				tmp[j].append(a[n-1-k][j])
		a = tmp
		tmp = n
		n = m
		m = tmp
	if r == 4:
		tmp = [[] for _ in range(m)]
		for j in range(m):
			for k in range(n):
				tmp[j].append(a[k][m-1-j])
		a = tmp
		tmp = n
		n = m
		m = tmp
	if r == 5:
		

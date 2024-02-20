

# 16931 겉넓이 구하기 - 분류해서 해결하기. 6면의 겉넓이를 나눠서 

n, m = map(int, input().split())

a = []

for _ in range(n):
	a.append(list(map(int, input().split())))

b = n * m
t = n * m

no = 0
e = 0
w = 0
s = 0

for i in range(m):
	no += a[0][i]
	s += a[n-1][i]

for i in range(n):
	e += a[i][m-1]
	w += a[i][0]

for i in range(n-1):
	for j in range(m):
		if a[i][j] < a[i+1][j]:
			no += a[i+1][j] - a[i][j]

for i in range(n-1):
	for j in range(m):
		if a[n-i-1][j] < a[n-i-2][j]:
			s += a[n-i-2][j] - a[n-i-1][j]

for i in range(n):
	for j in range(m-1):
		if a[i][j] < a[i][j+1]:
			w += a[i][j+1] - a[i][j]


for i in range(n):
	for j in range(m-1):
		if a[i][m-j-1] < a[i][m-j-2]:
			e += a[i][m-2-j] - a[i][m-1-j]

print(no + e + w + s + t + b)



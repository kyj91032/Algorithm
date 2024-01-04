
# 16967 배열 복원하기 -> 분류해서 해결

h, w, x, y = map(int, input().split())

b = []

for _ in range(h+x):
	b.append(list(map(int, input().split())))

a = [[0] * w for _ in range(h)]

for i in range(x):
	for j in range(w):
		a[i][j] = b[i][j]

for i in range(y):
	for j in range(h):
		a[j][i] = b[j][i]

for i in range(h, x+h):
	for j in range(y, w+y):
		a[i-x][j-y] = b[i][j]

for i in range(w, y+w):
	for j in range(x, x+h):
		a[j-x][i-y] = b[j][i]

for i in range(x, h): # a를 순서대로 갱신하면, 옮겨도 겹치는 부분이 자연스럽게 해결됨.
	for j in range(y, w):
		a[i][j] = b[i][j] - a[i-x][j-y]

for i in range(h):
	print(*a[i])

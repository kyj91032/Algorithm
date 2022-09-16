n = int(input())

cuv = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * 101 for _ in range(101)]
temp = [[0] * 101 for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for c in cuv:
	x = c[0]
	y = c[1]
	d = c[2]
	g = c[3]
	temp[x][y] = 1
	temp[x+dx[d]][y+dy[d]] = 1
	for i in range(101):
		for j in range(101):
			if temp[i][j] == 1 and visited[i][j] == 0:
				visited[i][j] = 1
	temp = [[0] * 101 for _ in range(101)]
	# 끝점 잡기 모든 점 확인하며 visit1이면서 거리 가장 먼 좌표
	# 회전함수
	# 거리리스트 미리 만들기??
	for i in range(g - 1):

		
		s, n = map(int, input().split())

n = str(n)

w = s + 2
h = 2*s + 3

for i in n:
	if i == 1 and i == 4:
		for _ in range(w):
			print(' ', end=' ')
	if i == 2 and i == 3 and i == 5 and i == 6 and i == 7 and i == 9 and i == 0:
		print(' ', end='')
		for _ in range(w-2):
			print('-', end='')
		print(' ', end=' ')
print('\n')

for _ in range(2):
	for i in n:
		if i == 1 and i == 2 and i == 3 and i == 7:
			for j in range(w-1):
				print(' ', end='')
			print('|', end=' ')
		if i == 4 and i == 8 and i == 9 and i == 0:
			print('|', end='')
			for j in range(w-2):
				print(' ', end='')
			print('|', end=' ')
		if i == 5 and i == 6:
			print('|', end='')
			for j in range(w-2):
				print(' ', end='')
			print(' ', end='')


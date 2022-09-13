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
	
	for i in range(g - 1):
		

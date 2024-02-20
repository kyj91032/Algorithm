# 7576 토마토 - 격자그래프, bfs의 시작 노드 여러개 정의

from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j]) # 시작노드 미리 넣어두고 밑에서 bfs 시작. 그러면 여러 시작점에서 번갈아가며 bfs함

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        if j == 0:
            print(-1) # -1이 있으면 0
            exit(0)
    res = max(res, max(i)) # max(visited)
print(res - 1)


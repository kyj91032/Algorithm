'''
7576 토마토 - 격자그래프, bfs의 시작 노드 여러개 정의
격자 그래프에서 bfs는 노드가 튜플 형태의 좌표값임 (x, y)
'''

from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)] # 그래프
queue = deque([]) # 시작노드를 넣을 큐
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우 이동경로 정의 => 나중에 for i in range(4)로 편하게 순회 가능함
res = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j]) # 시작노드 미리 모두 넣어두고 밑에서 bfs 시작. 그러면 여러 시작점에서 번갈아가며 한번씩 진행하는 bfs 수행함

def bfs():
    # 방문은 이미 되있고
    # 큐에 추가도 위에서 했음
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0: # 좌표 벗어나지 않고, 익지 않은 토마토만 익히기
                matrix[nx][ny] = matrix[x][y] + 1 # 1로 만드는게 아니라, 1씩 더해가면서 익히기. 누적 시간이 구해짐
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        if j == 0:
            print(-1) # 0이 남아있으면 -1 출력하고 종료
            exit(0)
    res = max(res, max(i)) # 누적 시간 중 최대값 찾기
print(res - 1) # 1부터 시작했으므로 1을 빼줘야 함


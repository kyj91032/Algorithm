
# 15685 드래곤 커브 - 이전 드래곤 커브 선을 거꾸로 확인하면서 90도 돌리며 추가해주면 된다. 는 아이디어... -> 현재 커브에 대한 방향 리스트


n = int(input())

graph = [[0] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n):

    y, x, d, g = map(int, input().split(' ')) # 리스트를 만들었을때, 주어진 y가 2차원 리스트의  인덱스임. 따라서 x y 바꿔줌
    graph[x][y] = 1 # 시작점 visited

    # 커브 리스트 만들기
    curve = [d]
    for j in range(g): # 세대만큼 반복
        for k in range(len(curve) - 1, -1, -1): # 커브 리스트 거꾸로 진행
            curve.append((curve[k] + 1) % 4) # 방향+1 하면서 커브 리스트 추가

    # 드래곤 커브 만들기
    for j in range(len(curve)): 
        x += dx[curve[j]] # 커브 리스트대로 방향 진행
        y += dy[curve[j]]
        if x < 0 or x >= 101 or y < 0 or y >= 101:
            continue
        graph[x][y] = 1 # 방문

answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1: # 오른쪽 밑 정사각형만을 모든 좌표에서 확인
            answer += 1

print(answer)

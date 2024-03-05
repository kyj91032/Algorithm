# BFS 격자그래프 기본유형
# 7567_토마토와 비슷함

from collections import deque

def solution(maps):
    
    queue = deque([(0,0)]) # 시작점
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]
    
    n = len(maps) # 열
    m = len(maps[0]) # 행
    
    def bfs():
        while queue:
            x, y = queue.popleft() 
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1 # 이동횟수 기록
                    queue.append((nx, ny))
                    
    bfs()
    
    if maps[n-1][m-1] == 1: # 도착점에 도달하지 못한 경우
        return -1
    else:
        return maps[n-1][m-1] # 도착점에 도달한 경우
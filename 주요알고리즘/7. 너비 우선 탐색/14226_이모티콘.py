# 14226 이모티콘 - 개수가 1000개면 2차원 가능성 높음. 처음에 [v][2]크기로 접근했다가 실패. 중복없이 횟수기록이 되게, (화면 이모티콘 개수, 클립보드 이모티콘 개수)를 리스트로.
# v*2는 특정 화면일때 클립값이 묶여있어서 모든 상태를 표현할 수 없음. 하지만 v*v는 특정화면일때 모든 클립값에 대해 횟수기록이 됨.

from collections import deque
n = int(input())
dist = [[-1] * (n + 1) for _ in range(n + 1)]
q = deque()
q.append((1, 0))  # 화면 이모티콘 개수, 클립보드 이모티콘 개수. 그리고 이 이차원 리스트에 방문처리를 하면서(횟수 기록) 탐색.
dist[1][0] = 0
while q:
    s,c = q.popleft()
    if dist[s][s] == -1: # 방문하지 않았으면
        dist[s][s] = dist[s][c] + 1 # 클립보드에 복사
        q.append((s, s))
    if s+c <= n and dist[s+c][c] == -1:
        dist[s+c][c] = dist[s][c] + 1 # 
        q.append((s+c, c))
    if s-1 >= 0 and dist[s-1][c] == -1:
        dist[s-1][c] = dist[s][c] + 1
        q.append((s-1, c))
answer = -1
for i in range(n+1):
    if dist[n][i] != -1:
        if answer == -1 or answer > dist[n][i]:
            answer = dist[n][i]
print(answer)

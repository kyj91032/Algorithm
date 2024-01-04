

# 18290 nm과 k (1)

def dfs(x, y, cnt, sum_value): # 재귀함수 정의
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)] # 탐색에 이용할 방향 정의
    if cnt == k: # 깊이에 따른 종료 조건
        global max_value
        max_value = max(max_value, sum_value) # 최댓값 갱신
        return
    for i in range(x, n): # 현재 줄 부터 탐색
        for j in range(y if i == x else 0, m): # 처음엔 y부터 m까지, 다음엔 0부터 m 까지 탐색
            if check[i][j]: # 현재 노드 방문 했다면 가지치기
                continue
            around = True
            for dx, dy in dxy: # 인접 노드 방문 했다면 가지치기
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m and check[nx][ny]:
                    around = False
                    break
            if around: # 방문하기
                around = 0
                check[i][j] = True
                dfs(i, j, cnt + 1, sum_value + item[i][j]) # 재귀 호출
                check[i][j] = False

n, m, k = map(int, input().split())
item = []
for _ in range(n):
    item.append(list(map(int, input().split())))

max_value = 0 # 최댓값 초기값
check = [[False for _ in range(m)] for _ in range(n)] # 방문 여부 테이블
dfs(0, 0, 0, 0)
print(max_value)


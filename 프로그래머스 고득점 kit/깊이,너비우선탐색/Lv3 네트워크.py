# 그냥 dfs 기본유형. 연결 개수 구하기
# visited를 초기화하지 않고 dfs를 모든 노드(방문한 노드 제외!!)를 순회하며 돌리면 됨

def solution(n, computers):
    
    graph = [[] for _ in range(n)] # 인접 리스트로 변환
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)
    
    visited = [False] * n # 방문 테이블
    def dfs(graph, visited, start): # dfs
        visited[start] = True
        for i in graph[start]:
            if not visited[i]:
                dfs(graph, visited, i)
    
    cnt = 0 # 네트워크 수 누적변수
    for i in range(n):
        if not visited[i]: # 순회하는데 방문한 노드는 순회하면 안됨 !!!!
            dfs(graph, visited, i)
            cnt += 1
        
    return cnt
    

# 플로이드-워셜 알고리즘: 모든 지점에서 다른 모든 지점까지의 최단 경로를 구하는 알고리즘이다.

# floyd-warshall의 구현
'''
floyd-warshall은 모든 지점끼리의 최단 경로를 구하며 재귀적으로 연결된 작은 문제를 반복적으로 해결함으로써 큰 문제를 해결하므로 기본적으로 구현에 기반한 다이나믹 프로그래밍이다.
dp 테이블은 비용을 데이터로 하는 인접 행렬 그래프 자체이며, 점화식은 Dab = min(Dab, Dak + Dkb) (k를 안 거치는 최소, 거치는 최소)
1. 인접 행렬 그래프를 초기화한다.
2. 점화식(Dab = min(Dab, Dak + Dkb)) (a부터 b까지 바로 가는 것보다 어떤 노드 k를 거쳐 가는 비용이 더 작다면 갱신하는 점화식)을 모든 경유점 k에 대해 반복하며 graph에 간선 정보 갱신.
모든 경유점 k에 대해 모든 경우(n-1P2)를 반복하므로 최단 거리 갱신이 보장된다. (경유한다면, 경유하지 않는다면, 모든 가능성을 고려해 최단 거리를 찾는 것이므로)
'''
# floyd-warshall 최단 경로

INF = int(1e9) 

n = int(input()) # 노드의 개수 n
m = int(input()) # 간선의 개수 m
graph = [[INF] * (n + 1) for _ in range(n + 1)] # 2차원 리스트로 그래프 인접 행렬 표현(distance 리스트 따로 안써도 됨), 모든 값을 무한으로 초기화 (초기에 최솟값을 넣기 위해). n + 1인 이유는 노드 번호와 인덱스 값을 맞추기 위해

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0 # 자기 자신과의 비용 0으로 초기화
      
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = c # 주어진 간선 정보 저장

for k in range(1, n + 1): # 모든 노드 k(1 ~ n)에 대하여
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) # n-1P2(= nP2)인 모든 조합을 점화식에 따라(다이나믹 프로그래밍) 최단 거리를 인접 행렬 graph에 갱신


      
# 11403 경로 찾기

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
for k in range(N):
    for i in range(N):
        for j in range(N): 
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1): # 최단거리 갱신이 아닌 모든 경로에서 모든 경로 갈 수 있는지 여부 확인
                graph[i][j] = 1
                
for row in graph:
    for col in row:
        print(col, end = " ")
    print()

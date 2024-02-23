# 다익스트라 알고리즘: 간선의 가중치가 양수인 그래프에서, 특정한 노드에서 출발하여 다른 모든 노드로 가는 각각의 최단 경로를 구해주는 알고리즘이다.

# Dijkstra의 구현 
'''
Dijkstra는 start로 시작하여 인접 노드 중 현재로서 최선의 거리인 노드 now를 확정지어 나가는 것이므로 기본적으로 그리디 알고리즘으로 분류된다.
또한 재귀적으로 연결된 작은 문제를 반복적으로 해결함으로써 큰 문제를 해결하므로 다이나믹 프로그래밍이기도 하다.
dp 테이블은 최단 거리 리스트, 점화식은 distance[w] = min(distance[w], distance[u] + weight[u][w])인 dp
1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택한다. # 선택된 노드는 최단거리 이미 확정
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 초기화한다. # 초기화 하면서 우선순위 큐에 삽입
5. 3, 4를 큐가 빌 때 까지 반복. (인접노드를 확인한다는 점은 BFS와 유사)
'''
    
# Dijkstra 최단 경로_ 우선순위 큐 O(ElogV)
# 우선순위 큐를 이용한다는 점에서 최단 경로 문제를 제외하고도 우선순위 큐를 필요로 하는 다른 문제 유형과도 흡사하다. ex) prim 알고리즘

import heapq # 우선순위 큐 라이브러리 (파이썬에서는 최소 힙) **힙은 삽입시간 logN, 삭제시간 logN. 리스트는 삽입시간 O(1), 삭제시간 O(N)
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1) # 최단거리 확정 테이블

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start):
  q = [] # 큐 생성
  heapq.heappush(q, (0, start)) # 시작 노드로 가기 위한 최단 경로를 0으로 설정하여 시작노드를 큐에 삽입.
  distance[start] = 0 # 시작 노드로 가기 위한 최단 경로는 0으로 설정
  while q: # 큐가 빌 때까지 반복
    dist, now = heapq.heappop(q) # 최소 큐로 가장 최단거리가 짧은 노드의 정보 꺼내기
    if distance[now] < dist: # 이미 처리된 적 있는 노드(최단거리 테이블의 값이 dist보다 작음)라면 무시. visited는 필요 없음
      continue
    for i in graph[now]: # now의 인접 노드 확인
      cost = dist + i[1] # 인접 노드까지의 비용 더함
      if cost < distance[i[0]]: # 더 작다면 최단 거리 테이블 갱신
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0])) # 갱신 후 우선순위 큐에 추가. 다음 최소 큐를 위해

dijkstra(start)

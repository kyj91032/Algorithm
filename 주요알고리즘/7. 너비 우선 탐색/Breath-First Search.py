'''
너비 우선 탐색(BFS): 가중치가 1인 그래프에서(모든간선의 가중치가 동일한 그래프에서), 탐색하지 않은 인접 노드를 우선으로 최대한 넓게 탐색하여 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색하는 방법이다.
선입선출 구조

BFS의 구현 방법

탐색 안했으면 탐색처리 하면서 큐에서 대기시키기
큐에서 빼면서 인접노드 순회하기
-- 너비 우선으로 탐색됨


'''

from collections import deque # 큐

graph = [ # 인접 리스트 방식.
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]


def bfs(graph, start, visited):
  visited[start] = True # 탐색 처리를 한다.
  queue = deque([start]) # 탐색 시작 노드를 큐에 enque하며 큐 선언
  while queue: # 큐가 빌떄까지
    v = queue.popleft() # 탐색한 노드를 큐에서 빼고
    ''' if 조건 추가 가능. 바로 return 하던지 등 '''
    for i in graph[v]: # 인접노드 순회
      if not visited[i]: # 탐색 안 했으면
        visited[i] = True # 탐색 처리
        queue.append(i) # 큐에 추가





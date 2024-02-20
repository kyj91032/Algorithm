# BF + DFS/BFS

# remove는 값 제거, pop은 인덱스 제거


def solution(n, wires):

    # BF
    # 1. 모든 전선을 한번씩 끊어보면서
    # 2. 둘로 나뉘었을때 노드 개수 차이의 max 갱신
        # DFS/BFS
        # 2-1. 둘로 나뉘었을 때 각각의 노드 개수 -> 그래프 탐색 필요 -> DFS or BFS 암거나 쓰면됨
        # 2-2. wires를 인접 리스트로 전환

    answer = n - 2
    for i in range(len(wires)): # BF: 모든 간선
        tmp = wires.copy()
        tmp.pop(i)
        new_wires = [[] for _ in range(n+1)]
        visited = [False] * (n+1)
        for w in tmp:
            new_wires[w[0]].append(w[1])
            new_wires[w[1]].append(w[0])
        for idx, g in enumerate(new_wires):
            if g != []: # n개의 송전탑 중 다른 송전탑과 연결된 송전탑을 시작점으로 지정
                start = idx
                break
        cnts = dfs(new_wires, start, visited)
        left_cnt = abs(n - cnts)
        if abs(cnts - left_cnt) < answer:
            answer = abs(cnts - left_cnt)

    return answer
            
def dfs(graph, v, visited):
    visited[v] = True
    cnt = 1
    for i in graph[v]:
        if not visited[i]:
            cnt += dfs(graph, i, visited) # cnt += 1 로하면 틀림
    return cnt
      
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

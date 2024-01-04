
# 2667 단지번호붙이기 - 격자그래프, dfs에서 깊이값 출력하기

n = int(input())

graph = []

for _ in range(n):
	graph.append(list(map(int, input())))
	# 간선 정보가 필요없는 그래프는 visited를 graph의 값으로 대신해서 쓴다. 격자그래프
num = []

def dfs(x, y):
	if x <= -1 or x >= n or y <= -1 or y >= n:
		return False
	if graph[x][y] == 1: # 시작 노드의 방문 여부로 dfs
		global count
		count += 1 # 스택이 다시 비었을때, count값이 유지되도록 해야함 그리고 다시 0으로 돌려주기
		graph[x][y] = 0
		dfs(x - 1, y)
		dfs(x, y - 1)
		dfs(x + 1, y)
		dfs(x, y + 1)
		return True
	return False

count = 0
result = 0
for i in range(n):
	for j in range(n): # 모든 노드를 확인하며 단지를 확인함. 아파트가 하나 발견되면 바로 단지를 정복하게됨.
		if dfs(i, j) == True:
			num.append(count) 
			count = 0 # (i, j) 에 대해 바로 count를 유지하면서 더해주며 단지를 정복하므로, 단지가 끝나면 dfs(i, j)가 종료되는데, 종료되면 count = 0으로 돌려주면 됨.
			result += 1
			
num.sort()
print(result)
for i in range(len(num)):
    print(num[i])



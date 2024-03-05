import sys
input = sys.stdin.readline

def find(parent, x):
	if parent[x] != x:
		parent[x] = find(parent, parent[x])
	return parent[x]

def union(parent, a, b):
	a = find(parent, a)
	b = find(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b
 
n, m = map(int, input().split()) # n: 도시의 개수, m: 도로의 개수

parent = [0] * (n + 1) # 노드 정보 초기화

for i in range(1, n + 1):
	parent[i] = i

edges = [] # 도로의 정보를 담을 리스트
result = 0

for _ in range(m):
	a, b, c = map(int, input().split()) # a, b: 도시의 번호, c: 도로의 길이
	edges.append((c, a, b)) # 도로의 길이를 기준으로 정렬하기 위해 튜플의 첫 번째 원소로 도로의 길이를 넣음

edges.sort() # 도로의 길이를 기준으로 정렬
last = 0

for edge in edges:
	c, a, b = edge
	if find(parent, a) != find(parent, b):
		union(parent, a, b)
		result += c
		last = c

print(result - last)
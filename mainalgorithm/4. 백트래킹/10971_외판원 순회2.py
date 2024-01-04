
# 10971 외판원 순회2

import sys
input = sys.stdin.readline

n = int(input())

w = [0]

for k in range(n):
	w.append(list(map(int, input().split())))
	w[k + 1].insert(0, 0)

INF = 10**9

def tsp(s): # 순회하며 합 계산
	sm = 0
	for j in range(len(s) - 1):
		if w[s[j]][s[j + 1]] != 0: # 갈 수 있는 경로인가 먼저 확인
			sm += w[s[j]][s[j + 1]]
			if sm >= res: # 가지치기: 합이 이미 최소를 넘었다면 넘기기
				return sm
		else: return INF
	if w[s[j + 1]][s[0]] != 0:
		sm += w[s[j + 1]][s[0]]
		return sm
	else: return INF

res = 10**9
s = []
def rec(): # 순회 경로 재귀로 구현
	global res
	if len(s) == n:
		res = min(res, tsp(s))
		return
	
	for i in range(1, n + 1):
		if i not in s:
			s.append(i)
			rec()
			s.pop()

rec()
print(res)

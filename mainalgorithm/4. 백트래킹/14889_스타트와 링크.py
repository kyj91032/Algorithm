
# 14889 스타트와 링크

from itertools import combinations

n = int(input())

s = [] #input

for _ in range(n):
	s.append(list(map(int, input().split())))

t = [] # rec stack
m = []

def rec(start):
	if len(t) == int(n/2):
		sum = 0
		c = list(combinations(t, 2)) # 리스트 t에서 조합 
		for k in c:
			sum += s[k[0] - 1][k[1] - 1] + s[k[1] - 1][k[0] - 1]
		m.append(sum)
		return
	
	for i in range(start, n + 1):
		t.append(i)
		rec(i + 1)
		t.pop()
rec(1)

m2 = []
l = len(m)

for j in range(int(l/2)):
	m2.append(abs(m[j] - m[l - 1 - j]))

print(min(m2))


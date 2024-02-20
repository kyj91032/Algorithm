
# 15661 링크와 스타트

from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input())

s = [] # input

for _ in range(n):
	s.append(list(map(int, input().split())))


t = [] # recstack
m = []


def rec(start, k):
	if len(t) == k:
		if k == 1:
			m.append(0)
		else:
			sum = 0
			c = list(combinations(t, 2))
			for k in c:
				sum += s[k[0] - 1][k[1] - 1] + s[k[1] - 1][k[0] - 1]
			m.append(sum)
		return
		
	for i in range(start, n + 1):
		t.append(i)
		rec(i + 1, k)
		t.pop()

for p in range(1, n):
	rec(1, p)

m2 = []
l = len(m)

for j in range(int(l/2)):
	m2.append(abs(m[j] - m[l - 1 - j]))

print(min(m2))





# 10819 차이를 최대로 - 최대최소 bf

import sys
input = sys.stdin.readline

def np(pl): # next permutation 알고리즘 (재귀로 구현하는 순열보다 빠름.)
	x = 0
	for i in range(len(pl) - 1, 0, -1):
		if pl[i - 1] < pl[i]:
			x = i - 1
			break
	for i in range(n - 1, 0, -1):
		if pl[x] < pl[i]:
			pl[x], pl[i] = pl[i], pl[x]
			pl = pl[:x + 1] + sorted(pl[x + 1:])
			return pl
	return [-1]


n = int(input())
a = list(map(int, input().split()))

a.sort()

ans = 0 # 최대값 저장, 최신화

s = 0
for j in range(len(a) - 1):
    s += abs(a[j] - a[j+1])
if s > ans:
    ans = s

arr = a

while 1:
	arr = np(arr)
	if arr == [-1]:
		break
	s = 0

	for j in range(len(arr) - 1):
		s += abs(arr[j] - arr[j+1])
	if s > ans:
		ans = s
print(ans)



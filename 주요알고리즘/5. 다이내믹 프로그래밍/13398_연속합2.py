
# 13398 연속합2 - 어떤 걸 가지고 다음 i에 대한 d를 만들 수 있는지. 지운 경우dp와 안지운 경우dp를 나눠야했고 2차원 dp테이블 사용

n = int(input())

a = list(map(int, input().split()))

d = [[0] * 2 for i in range(n + 1)]

t = 0
for j in range(n):
	if a[j] > 0:
		t = 1

if t == 1:
	for i in range(1, n + 1):
		if d[i-1][0] + a[i-1] > 0:
			d[i][0] = d[i-1][0] + a[i-1]
		else: d[i][0] = 0

	for i in range(2, n + 1):
		d[i][1] = max(d[i-1][1] + a[i-1], d[i-1][0])
	
	m = 0
	for i in range(n + 1):
		for j in range(2):
			m = max(m, d[i][j])
	
	print(m)
else:
	print(max(a))
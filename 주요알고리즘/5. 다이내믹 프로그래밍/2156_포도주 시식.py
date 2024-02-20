

# 2156 포도주 시식 - 2차원 dp 테이블. 점화식이 이전의 i 에 대해 어떤 정보를 요구하는가? 자기자신을 포함해서 나온 최댓값, 자기자신을 제외하고 나온 최댓값. 두 가지 모두 구하기.

n = int(input())

a = [0]
for _ in range(n):
	a.append(int(input()))

d = [[0] * 2 for _ in range(n+1)]

if n == 1:
	d[1][0] = 0
	d[1][1] = a[1]
	print(a[1])
elif n == 2:
	d[1][0] = 0
	d[1][1] = a[1]
	d[2][0] = a[1]
	d[2][1] = a[2] + a[1]
	print(a[1] + a[2])
else:
	d[1][0] = 0
	d[1][1] = a[1]
	d[2][0] = a[1]
	d[2][1] = a[2] + a[1]
	for i in range(3, n+1):
		for j in range(2):
			if j == 0:
				d[i][j] = max(d[i-1])
			if j == 1:
				d[i][j] = a[i] + max(a[i-1] + d[i-2][0], d[i-2][1])
	print(max(d[n]))

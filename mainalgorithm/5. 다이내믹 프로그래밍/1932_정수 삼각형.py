
# 1932 정수 삼각형 - 2차원 dp 테이블. 점화식이 이전 i에 대해 더 디테일한 정보를 요구할 때, 자기 자신을 포함했는지를 기준으로 나눠 구하는 d.

n = int(input())

t = []
for _ in range(n):
	t.append(list(map(int, input().split())))

d = [[] for _ in range(501)]
for i in range(501):
	for j in range(i+1):
		d[i].append(0)

if n == 1: # 이렇게 분류 안하면 indexerror 뜸
	d[0] = t[0][0]
	print(d[0])
elif n == 2:
	d[1][0] = t[1][0] + d[0]
	d[1][1] = t[1][1] + d[0]
	print(max(d[1]))
else:
	d[0] = t[0][0]
	d[1][0] = t[1][0] + d[0]
	d[1][1] = t[1][1] + d[0]
	for i in range(2, n):
		for j in range(i+1):
			if j == 0:
				d[i][j] = t[i][j] + d[i-1][j]
			elif j == i:
				d[i][j] = t[i][j] + d[i-1][j-1]
			else:
				d[i][j] = t[i][j] + max(d[i-1][j-1], d[i-1][j])
	print(max(d[n-1]))

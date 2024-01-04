
# 11057 오르막 수 - 2차원 dp 테이블.

n = int(input())

d = [[0] * 11 for _ in range(1000)]

for k in range(10):
	d[0][k] = 1

d[0][10] = 10

for i in range(1, n):
	
	d[i][0] = d[i - 1][10] % 10007
	
	for j in range(1, 10):
		d[i][j] = d[i][j - 1] % 10007 - d[i - 1][j - 1] % 10007
		
	d[i][10] = sum(d[i])

print(d[n - 1][10] % 10007)


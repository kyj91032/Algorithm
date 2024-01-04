
# 2193 이친수 - 2차원 dp 테이블

n = int(input())

d = [[0 for i in range(2)] for j in range(91)] # 자리수를 i, d를 개수로 했을때, 0으로 끝나는 개수, 1로 끝나는 개수의 정보가 필요하므로, 2차원 dp 테이블 사용(j 추가)

d[1][0] = 0
d[1][1] = 1

d[2][0] = 1
d[2][1] = 0

for i in range(3, 91):
	for j in range(2):
		if j == 0: # 0으로 끝나는 개수 점화
			d[i][j] = d[i-1][j] + d[i-1][1]
		if j == 1: # 1로 끝나는 개수 점화
			d[i][j] = d[i-1][0]
print(sum(d[n]))

# 1149 RGB거리 - 2차원 dp 테이블. 점화식이 더 많은 정보를 요구. 단순히 전의 d값이 아닌, 그 d가 d[i][0]인지 d[i][1]인지 d[i][2]인지. 무슨 색으로 끝났는지

n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))

for i in range(1, len(p)):
    p[i][0] = min(p[i - 1][1], p[i - 1][2] ) + p[i][0] # 그냥 빨강 초록 파랑 모두에 대해 최솟값을 구해버림.
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]

print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))
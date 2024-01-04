
# 1309 동물원 - 2차원 dp 테이블. 점화식이 더 많은 정보를 요구. 단순히 전의 d값이 아닌, 그 d가 d[i][0]인지 d[i][1]인지 d[i][2]인지. 사자가 어디에 있는지.

import sys
input = sys.stdin.readline
n = int(input())
dp = [0]*(n+1)
for i in range(n+1) :
    dp[i] = [0,0,0]
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1

for i in range(2, n + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901

print(sum(dp[n]) % 9901)


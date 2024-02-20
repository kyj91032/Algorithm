
# 15988 1, 2, 3 더하기3 - 규칙성에 따른 dp

import sys
input = sys.stdin.readline

dp = [0 for i in range(1000001)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 1000001):
    dp[i] = dp[i - 1] % 1000000009 + dp[i - 2] % 1000000009 + dp[i - 3] % 1000000009 # 그냥 나열 후 규칙에 의한 점화식

t = int(input())
for i in range(t):
    n = int(input())
    print(dp[n] % 1000000009)

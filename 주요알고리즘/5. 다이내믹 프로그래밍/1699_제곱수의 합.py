
# 1699 제곱수의 합 - dp와 살짝 빡센 구현.

n = int(input())
	     
dp = [0 for i in range(n + 1)]
square = [i * i for i in range(1, 317)] # 초기 점화식을 세울 때 제곱수의 정보가 필요해서.
	     
for i in range(1, n + 1):
    s = []
    for j in square:
        if j > i: # i보다 큰 제곱수 거르기
            break
        s.append(dp[i - j]) # s에 i보다 작은 제곱수를 제거한 개수 넣기.
    dp[i] = min(s) + 1 # 그 s중에 최소개수 + 1이 dp값.  i=7 같은 경우에는 그게 그건데, i=8과 같이 2제곱 2개로 표현될 때는 이게 맞음.
print(dp[n])

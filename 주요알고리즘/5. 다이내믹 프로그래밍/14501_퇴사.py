
# 14501 퇴사 - 초기 점화식부터, 그걸 구체화시키는 과정. 그리고 dp 테이블이 뒤에서부터 정복.

N = int(input())
arr = []
for _ in range(N):
    day, pay = map(int, input().split())
    arr.append((day, pay))
dp = [0] * (N+1) # 주어진 표에서, d[i]는 현재 i일일때 얻을 수 있는 최대 수익으로 정의.
	     
# 그럼 결국 초기 점화식은 d[i] = max(d(i + T[i]) + P[i], d(i + 1)) i번째에 상담을 했을 때(d[i+T[i]]에서 이와 똑같이) or i번째에 상담을 건넜을 때(i+1에서 이와 똑같이 d[i+1])

for i in range(N - 1, -1, -1): # 초기 점화식을 고려하여 i를 뒤에서부터 진행하며 dp 테이블을 완성한다.
    day = arr[i][0]
    pay = arr[i][1]
    if day + i <= N: # i가 현재 날짜. 현재날짜 + day(상담 걸리는 기간)이 n을 넘지 않으면, 
        dp[i] = max(pay + dp[day+i], dp[i+1]) # 현재 상담하는 경우 or 다음날 상담하는 경우
    else:
        dp[i] = dp[i+1]

print(dp[0])
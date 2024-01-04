
# 14002 가장 긴 증가하는 부분수열4 - 초기 점화식을 세울 때, 모든 경우가 고려되는가를 잘 확인.

N = int(input())

A = list(map(int, input().split()))

# 수열이 ai까지일때 가장 긴 부분수열의 길이를 d[i]라고 정의.
# 추상적인 점화식 : d[i] = if a[j] < a[i] 일때만 dp[j] + 1와 d[i]중(이건 왜?) max로 갱신.

dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp)) # 테이블 중 최댓값.

s = [] # 수열 담을 리스트
t = max(dp) # t를 줄여가며 수열 담을 것
for i in range(N - 1, -1, -1):
    if dp[i] == t:  # 만약 dp[i] 값이 t값과 같다면
        s.append(A[i])  # 해당 A[i]값을 s에 추가
        order -= 1  # 해당 order 값을 1씩 감소시킨다.

s.reverse()  # 큰수부터 작은수로 뽑았기 때문에 반대로 정렬
print(s) # 정답수열 출력

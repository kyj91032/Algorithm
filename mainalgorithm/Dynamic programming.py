# 다이내믹 프로그래밍: 완전 탐색 시, 재귀적으로 연결된 작은 문제를 반복적으로 해결(결과값의 재사용)함으로써 큰 문제를 해결할 수 있을 때 사용한다.
# 초기값부터 i까지 모두 재귀적으로 영향을 주고 있어 한번에 필드를 정복한다. (=> 점화식과 dp 테이블 필요)

# 다이내믹 프로그래밍의 기본 동작 과정

1. i와 d[i]를 정의한다.
2. 초깃값을 준 후,
3. 일반적인 i를 생각하며 필드가 정복되는 점화식을 구한다.


# 탑 다운 방식. 재귀 f 함수 기반 점화식

d = [0] * 100 # 메모이제이션을 위한 리스트

def fibo(x):
  print('f(' + str(x) + ')', end = ' ')
  if x == 1 or x == 2: # 종료조건
    return 1
  if d[x] != 0: # 메모이제이션
    return d[x]
  d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


# 바텀 업(상향식) 방식. 반복 a 수열 기반 점화식

d = [0] * 100 # 1. d[i]는 i번째 수열의 항으로 정의.

d[1] = 1 # 2. 초기값
d[2] = 1

for i in range(3, 100) 
  d[i] = d[i - 1] + d[i - 2] # 3. 점화식



# 1로 만드는 최소 연산

x = int(input())
d = [0] * 30001 # 1. d[i]는 정수 i를 1로 만드는 최소 연산 횟수로 정의
		# 2. 초깃값 설정

for i in range(2, x + 1): 
  d[i] = d[i - 1] + 1  # d[i]의 최소를 구하기 위한 초깃값. bruteforce
  if i % 2 == 0:
    d[i] = min(d[i], d[i // 2] + 1) # 3. 일반적인 i를 생각하며 필드가 정복되는 점화식: ai = max(ai-1, ai/2, ai/3, ai/5) + 1
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)
  if i % 5 == 0:
    d[i] = min(d[i], d[i // 5] + 1) # 모든 경우 확인하며 최신화해서 d[i]의 최솟값 구하기. bruteforce

print(d[x])


# 식량 많이 털기

n = int(input())
array = list(map(int, input().split())

d = [0] * 100 # 1. d[i]는 i번째 창고까지의 최대 식량으로 정의

d[0] = array[0]
d[1] = max(array[0], array[1]) # 2. 초깃값
for i in range(2, n):
  d[i] = max(d[i - 1], d[i - 2] + array[i]) # 3. 점화식: ai = max(ai-1, ai-2 + ki)

print(d[n - 1])             


# 최소 화폐 단위 구성: 단위마다 d.p 반복

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))
# f(i) = ai = i원의 화폐 구성 최적의 해
# 점화식: for(ai = min(ai, ai-k + 1))

d = [10001] * (m + 1) # 

d[0] = 0   # 초깃값
for i in range(n):  # 단위마다 dp를 반복
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:  # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1) # 최소 선택.

if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
             

# 최소 화폐 단위 구성: 단위 한꺼번에 d.p

n, m = map(int, input().split())

array = []
for _ in range(n):
	array.append(int(input()))
	
d = [10001] * (m + 1)

d[0] = 0

for i in range(array[0], m + 1):
	for j in range(0, n):
		if i - array[j] >= 0:
			d[i] = min(d[i], d[i - array[j]] + 1)
	if d[i] == 10001:
		print(-1)
		break

if d[i] != 10001:
	print(d[m])
             

# 타일을 배치하는 경우의 수

N = int(input())

d = [0] * 1001 # 1. d[i]는 i까지의 타일 배치의 경우의 수로 정의

d[0] = 0
d[1] = 1
d[2] = 3 # 2. 초깃값

for i in range(3, N + 1):
	d[i] = d[i - 2] * 2 + d[i - 1] # 3. 점화식: ai = ai-2 * 2 + ai-1.

print(d[N])


# 14501 퇴사 ?? 이걸 어케 생각해.. 재귀 bf가 현실적

n = int(input())
T = [0]
P = [0]
for _ in range(n):
    a,b = map(int,input().split())
    T.append(a)
    P.append(b)

d = [0 for _ in range(n + 1)] # 1. i번째 날까지 최대 상담 보수 d[i]
			      # 2. 초기값 d[0] = 0, ..
for i in range(1, n + 1):
    d[i] = max(d[i], d[i - 1]) # 마지막에 일수 초과할 때 테이블 완성하기 위한 코드
    if i + T[i] - 1 <= n: # 일수 초과하지 않을 때
        dp[i + T[i] - 1] = max(dp[i + T[i] - 1], dp[i - 1] + P[i]) # 3. 점화식: d[오늘 꺼 상담 범위까지의 d[] 값] = max(
print(dp[-1])


# 11052 카드 구매하기 - bf + dp의 사고과정

n = int(input())
p = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1): # 바텀 업 방식으로 dp 테이블 완성
	for k in range(1, i + 1):
		dp[i] = max(dp[i], dp[i-k] + p[k - 1]) # 점화식을 반복해서 적용해야 비로소 정복되는 유형. 이중 반복문을 이용했다.
						       # d를 통해 자연수의 분할을 압축시킬 수 있었다.
print(dp[i])


# 15990 1, 2, 3 더하기 - 2차원 dp 테이블

# 1,2,3으로 끝난 갯수를 세고 그 뒤에 해당하는 숫자 붙여나가며 정복.

import sys
input=sys.stdin.readline

tc = int(input())

dp=[[0 for _ in range(3)] for i in range(100001)]

dp[1]=[1,0,0] # 1은 1로 끝나는 거 하나
dp[2]=[0,1,0] # 2는 2로 끝나는 거 하나
dp[3]=[1,1,1] # 3은 1로 끝나는 거 하나(2 + 1), 2로 끝나는 거 하나(1 + 2), 3으로 끝나는 거 하나(3)

for i in range(4,100001): # 4부터 dp테이블 생성
    # 6일때 만약

    # 5에서 2와 3으로 끝난거에 1 붙이기
    dp[i][0] = dp[i-1][1] % 1000000009 + dp[i-1][2] % 1000000009
    # 4에서 1과 3으로 끝난거에 2붙이기
    dp[i][1]=dp[i-2][0] % 1000000009 + dp[i-2][2] % 1000000009
    # 3에서 1과 2로 끝난거에 3붙이기
    dp[i][2] = dp[i-3][0] % 1000000009 + dp[i-3][1] % 1000000009

for i in range(tc):
    n = int(input())
    print(sum(dp[n]) % 1000000009)


# 10844 쉬운 계단 수 - 2차원 dp 테이블

n = int(input())

dp = [[0 for i in range(10)] for j in range(101)]

for i in range(1, 10): # 각 자리수에서 맨 뒤에 올수 있는 숫자의 개수로 dp 테이블 두기. 자리수를 i, 맨 뒤 숫자를 j로, d값은 개수.
    dp[1][i] = 1 # n = 1(i = 1)일 때 초기값 부여

for i in range(2, n + 1): # i = 2부터 바텀 업.
    for j in range(10): # j는 0부터 9까지 확인하면서 개수 갱신
        if j == 0:
            dp[i][j] = dp[i - 1][1] # 0으로 끝나는 수의 개수는 i - 1에서 1로 끝나는 수의 개수
        elif j == 9:
            dp[i][j] = dp[i - 1][8] # 9로 끝나는 수의 개수는 i - 1에서 8로 끝나는 수의 개수
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1] # j가 1~8일땐 i - 1에서 j - 1로 끝나는 수의 개수 + j + 1로 끝나는 수의 개수
print(sum(dp[n]) % 1000000000)


# 2193 이친수 - 2차원 dp 테이블

n = int(input())

d = [[0 for i in range(2)] for j in range(91)] # 자리수를 i, d를 개수로 했을때, 0으로 끝나는 개수, 1로 끝나는 개수가 따로 정복되므로 2차원 dp 테이블 사용(j 추가)

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


# 14002 가장 긴 증가하는 부분수열4 - bf(최대최소, 이중반복) + dp의 사고 과정

N = int(input())

A = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i): # 점화식을 반복해서 적용해야 비로소 정복되는 유형. 이중 반복문을 이용했다.
        if A[j] < A[i]: # 이전의 a값을 확인하며 작은 것 중 최대 길이 + 1로 갱신한다
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

s = [] # 수열 담을 리스트
t = max(dp) # t를 줄여가며 수열 담을 것
for i in range(N - 1, -1, -1):
    if dp[i] == t:  # 만약 dp[i] 값이 t값과 같다면
        s.append(A[i])  # 해당 A[i]값을 s에 추가
        order -= 1  # 해당 order 값을 1씩 감소시킨다.

s.reverse()  # 큰수부터 작은수로 뽑았기 때문에 반대로 정렬
print(s) # 정답수열 출력


# 1912 연속 합 - dp, 점화식의 아이디어..

n = int(input())

arr = list(map(int, input().split()))
dp = [0] * len(arr)
dp[0] = arr[0]

for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i-1] + arr[i]) # arr[i]와 dp를 비교해나가면 된다는 걸 어떻게 알지..?

print(max(dp))


# 1699 제곱수의 합 -

n = int(input())
	     
dp = [0 for i in range(n + 1)]
square = [i * i for i in range(1, 317)]
	     
for i in range(1, n + 1):
    s = []
    for j in square: # in 활용.. 반복문
        if j > i: # i보다 작거나 같은 제곱수
            break
        s.append(dp[i - j]) # s에는 dp(i - i보다 작거나 같은 제곱수)가 들어감.. 뭘 하든 상관 없는거 아닌가.. 이걸 어떻게 생각하지
    dp[i] = min(s) + 1 # 그중에 최소 + 1이 dp값
print(dp[n])


# 2225 합분해 - dp를 대하는 자세

'''table(2, 3) 은 값 2를 만들기 위해 3개의 숫자를 더해서 만드는 경우의 수를 의미하며 다음과 같이 나타낼 수 있다.
 
(0을 1개의 숫자로 만드는 경우의 수)*(2를 2개의 숫자로 만드는 경우의 수)
 + (1을 1개의 숫자로 만드는 경우의 수)*(1을 2개의 숫자로 만드는 경우의 수)
+ (2를 1개의 숫자로 만드는 경우의 수)*(0을 2개의 숫자로 만드는 경우의 수)
 = table(0, 1)*table(2, 2) + table(1, 1)*table(1, 2) + table(2, 1)*table(0, 2)
 = table(2, 2) + table(1, 2) + table(0, 2)
 
즉 어차피 앞에 더해지는 값은 1개를 이용한다고 생각했기 때문에 뒤에 더해지는 나머지의 경우만 찾으면 된다.
그 결과 table(n, k) = table(n, k-1) + table(n-1, k-1) + ... + table(0, k-1) 이라는 식이 나오게 된다.
게다가 여기서 table(n-1, k) = table(n-1, k-1) + ... + table(0, k-1) 이기 때문에, 처음의 식은 다음과 같이 나오게 된다.
table(n, k) = table(n, k-1) + table(n-1, k)
'''
	     
import sys

N, K = map(int, sys.stdin.readline().split())
mod = 1000000000
table = [1]
table += [0] * N

for _ in range(1, K+1):
    for idx in range(1, N+1):
        table[idx] = (table[idx] + table[idx-1])%mod

sys.stdout.write(str(table[N]))


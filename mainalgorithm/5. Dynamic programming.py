# 다이내믹 프로그래밍: 여러 개의 부분 문제로 쪼개지며, 작은 문제의 답을 모아서 큰 문제를 해결할 수 있고, 동일한 작은 문제를 반복적으로 해결해야 할 때의 문제 해결 방법이다.

# 다이내믹 프로그래밍의 구현 방법

# 1. 완전 탐색을 시도했을 때, 여러 개의 부분 문제로 쪼개지는 구조이며 그 결과값을 재사용함으로써 큰 문제를 해결할 수 있다면.(= 점화식이 세워진다면) -> dp임.
# 2. d와 i를 정의한다
# 3. 어떤 걸 가지고 다음 i에 대한 d를 만들어낼 수 있는지를 구현한다


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

for i in range(3, 100):
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
array = list(map(int, input().split()))

d = [0] * 100 # 1. d[i]는 i번째 창고까지의 최대 식량으로 정의

d[0] = array[0]
d[1] = max(array[0], array[1]) # 2. 초깃값
for i in range(2, n):
  d[i] = max(d[i - 1], d[i - 2] + array[i]) # 3. 점화식: ai = max(ai-1, ai-2 + ki)

print(d[n - 1])             


# 최소 화폐 단위 구성 - 초기 점화식을 고려했을 때, dp 테이블이 순서대로 완성되지 않고, 않아도 영향이 없음. 화폐 2에 대해서 dp 실행 후 3에 대해서 dp ...

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))
# f(i) = ai = i원의 화폐 구성 최적의 해
# 점화식: for(ai = min(ai, ai-k + 1))
# 점화식에 변수 k 를 고정시켜야함. 따라서 k를 고정시켜가며 테이블을 구성.

d = [10001] * (m + 1) # 과정이 끝났음에도 10001로 남아있다면 화폐구성이 가능하지 않다는 의미.

d[0] = 0   # 초깃값
for k in array:  # k를 고정. 점화식을 위해
    for j in range(k, m + 1): # j는 화폐부터 m까지
        d[j] = min(d[j], d[j - k] + 1) # 최소 선택 (점화식)

if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
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


# 11052 카드 구매하기 - 점화식에 변수가 추가되어 이중 반복문이 되었다.

n = int(input())
p = list(map(int, input().split()))
dp = [0] * (n + 1)
	     
# 초기 점화식 : 3개 되기 위한 금액최소 = min(2개 되기 위한 금액 최소 + p1, 1개 되기 위한 금액 최소 + p2)

for i in range(1, n + 1): # 바텀 업 방식으로 dp 테이블 완성
	for k in range(1, i + 1):
		dp[i] = max(dp[i], dp[i-k] + p[k - 1]) # 일반적인 점화식
print(dp[i])


# 15990 1, 2, 3 더하기 - 2차원 dp 테이블. 점화식이 더 많은 정보를 요구.

# 1,2,3으로 끝난 갯수를 세고 그 뒤에 해당하는 숫자 붙여나가며 정복.

import sys
input = sys.stdin.readline

tc = int(input())

# 추상적인 점화식 : 4를 1,2,3의 합으로 나타내는 방법의 수 d[4] = 1에서 1과 2로 끝난거에 3붙이기 + 2에서 1과 3으로 끝난거에 2붙이기 + 3에서 1과 2로 끝난거에 1붙이기
	     
dp=[[0 for _ in range(3)] for i in range(100001)] # 추상적인 점화식에 따라 dp 테이블이 2차원으로 형성되었다. 단순히 dp 값이 방법의 수인게 아니라, 더 많은 정보 즉, 그 방법의 수 중에서 1로 끝나는 것, 2로 끝나는 것, 3으로 끝나는 것의 개수를 나눠서 저장한 것이다.

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


# 10844 쉬운 계단 수 - 2차원 dp 테이블. 점화식이 더 많은 정보를 요구.

n = int(input())

# 추상적인 점화식이 단순히 계단 수의 개수만이 아닌 각각의 끝자리에 따른 개수까지 필요로 함. 따라서 2차원 dp 테이블 생성.
	     
dp = [[0 for i in range(10)] for j in range(101)]

for i in range(1, 10):
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


# 1912 연속 합 - if를 써야할까 max()로 충분할까?

n = int(input())

arr = list(map(int, input().split()))
dp = [0] * len(arr)
dp[0] = arr[0]

for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i-1] + arr[i]) # 점화식 : max(i번째 수를 선택 안함, i번째 수를 선택함)

print(max(dp))


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


# 2225 합분해 - 복잡한 점화식 세우기

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
# 애초에 i와 d를 정의할 때, 변수 자체가 2개. n과 k
	     
import sys

N, K = map(int, sys.stdin.readline().split())
mod = 1000000000
table = [1]
table += [0] * N

for _ in range(1, K+1):
    for idx in range(1, N+1):
        table[idx] = (table[idx] + table[idx-1])%mod

sys.stdout.write(str(table[N]))


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



# 2156 포도주 시식 - 2차원 dp 테이블. 점화식이 이전의 i 에 대해 어떤 정보를 요구하는가? 자기자신을 포함해서 나온 최댓값, 자기자신을 제외하고 나온 최댓값. 두 가지 모두 구하기.

n = int(input())

a = [0]
for _ in range(n):
	a.append(int(input()))

d = [[0] * 2 for _ in range(n+1)]

if n == 1:
	d[1][0] = 0
	d[1][1] = a[1]
	print(a[1])
elif n == 2:
	d[1][0] = 0
	d[1][1] = a[1]
	d[2][0] = a[1]
	d[2][1] = a[2] + a[1]
	print(a[1] + a[2])
else:
	d[1][0] = 0
	d[1][1] = a[1]
	d[2][0] = a[1]
	d[2][1] = a[2] + a[1]
	for i in range(3, n+1):
		for j in range(2):
			if j == 0:
				d[i][j] = max(d[i-1])
			if j == 1:
				d[i][j] = a[i] + max(a[i-1] + d[i-2][0], d[i-2][1])
	print(max(d[n]))


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


	     
# 11055 가장 큰 증가 부분 수열 - 시간복잡도에 대해.. n이 10000까지는 이중 반복 가능성 있음

n = int(input())
	     
array = list(map(int, input().split()))

d = [1] * n
d[0] = array[0]
for i in range(1, n):
  for j in range(i): # 일차원 반복문으로 코드를 짜면, 앞 쪽이 고려되지 않는 걸 알 수 있는데, 이 때 n의 크기를 보고 이중 반복문을 활용할 생각을 해야함.
    if array[j] < array[i]:
      d[i] = max(d[i], d[j] + array[i]) # ai가 더 크면 이전 d에 넣어보고
    else:
      d[i] = max(d[i], array[i]) # ai가 더 작으면 ai만 넣어보고

print(max(d))




# 11722 가장 긴 감소하는 부분수열 - i가 추가됨에 따라 점화식이 이전 i에 대해 뭘 요구하는지를 파악하는 과정에서, 이중 반복문이 필요했고, 시간복잡도까지 확인해주기(n < 1000)

n = int(input())

a = list(map(int, input().split()))

d = [1] * n # 사소한 초깃값 설정. d = [0]*n 으로 하면 틀림. 다른 반례에 걸려서..

d[0] = 1

for i in range(1, n):
	for j in range(i):
		if a[j] > a[i]:
			d[i] = max(d[i], d[j] + 1)
print(max(d))

	     

# 11054 가장 긴 바이토닉 부분 수열 - 기준 인덱스의 좌측은 증가하는 부분수열, 우측은 감소하는 부분수열의 reverse를 구해서 합한 길이가 가장 긴 순간의 인덱스. 애초에 바이토닉을 한번에 구할 수가 없었다..

N = int(input())

List = list(map(int, input().split()))

dp1 = [1] * N
dp2 = [1] * N

sub_len = [0] * N

Max = 0

for i in range(N):
    for j in range(i):
        if List[i] > List[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
	  
	     
List.reverse()

for i in range(N):
    for j in range(i):
        if List[i] > List[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
dp2.reverse()

for i in range(N):
    sub_len[i] = dp1[i] + dp2[i]

print(max(sub_len) - 1)



# 13398 연속합2 - 어떤 걸 가지고 다음 i에 대한 d를 만들 수 있는지. 지운 경우dp와 안지운 경우dp를 나눠야했고 2차원 dp테이블 사용

n = int(input())

a = list(map(int, input().split()))

d = [[0] * 2 for i in range(n + 1)]

t = 0
for j in range(n):
	if a[j] > 0:
		t = 1

if t == 1:
	for i in range(1, n + 1):
		if d[i-1][0] + a[i-1] > 0:
			d[i][0] = d[i-1][0] + a[i-1]
		else: d[i][0] = 0

	for i in range(2, n + 1):
		d[i][1] = max(d[i-1][1] + a[i-1], d[i-1][0])
	
	m = 0
	for i in range(n + 1):
		for j in range(2):
			m = max(m, d[i][j])
	
	print(m)
else:
	print(max(a))

	     

# 2133 타일 채우기 - 이중 반복을 염두하고, 규칙적인 증가의 증가를 파악했어야함.

N = int(input())

d = [0] * 31
d[0] = 1

for i in range(2, N + 1, 2):
    d[i] = d[i - 2] * 3
    for j in range(0, i - 2, 2):
        d[i] += d[j] * 2

print(d[N])


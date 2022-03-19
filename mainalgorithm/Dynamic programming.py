# 다이내믹 프로그래밍: 완전 탐색 시, 재귀적으로 연결된 작은 문제를 반복적으로 해결함으로써 큰 문제를 해결할 수 있을 때 사용한다.
# 초기값부터 i까지 모두 재귀적으로 영향을 주고 있어 한번에 필드를 정복한다. (=> 점화식과 dp 테이블 필요)

# 다이내믹 프로그래밍의 기본 동작 과정
'''
1. i와 d[i]를 정의한다.
2. 초깃값을 준 후,
3. 일반적인 i를 생각하며 필드가 정복되는 점화식을 구한다.
'''

''' 탑 다운 방식. 재귀 f 함수 기반 점화식

d = [0] * 100 # 메모이제이션을 위한 리스트

def fibo(x):
  print('f(' + str(x) + ')', end = ' ')
  if x == 1 or x == 2: # 종료조건
    return 1
  if d[x] != 0: # 메모이제이션
    return d[x]
  d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]
'''

''' 바텀 업(상향식) 방식. 반복 a 수열 기반 점화식

d = [0] * 100 # 1. d[i]는 i번째 수열의 항으로 정의.

d[1] = 1 # 2. 초기값
d[2] = 1

for i in range(3, 100) 
  d[i] = d[i - 1] + d[i - 2] # 3. 점화식
'''


''' 1로 만드는 최소 연산

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
'''


''' 식량 많이 털기

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
'''
             
             
''' 타일을 배치하는 경우의 수

N = int(input())

d = [0] * 1001 # 1. d[i]는 i까지의 타일 배치의 경우의 수로 정의

d[0] = 0
d[1] = 1
d[2] = 3 # 2. 초깃값

for i in range(3, N + 1):
	d[i] = d[i - 2] * 2 + d[i - 1] # 3. 점화식: ai = ai-2 * 2 + ai-1.

print(d[N])
'''


''' 14501 퇴사 ?? 이걸 어케 생각해.. 재귀 bf가 현실적

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
'''

'''
다이내믹 프로그래밍: 여러 개의 부분 문제로 쪼개지며, 작은 문제의 답을 모아서 큰 문제를 해결할 수 있고, 동일한 작은 문제를 반복적으로 해결해야 할 때의 문제 해결 방법이다.

다이내믹 프로그래밍의 구현 방법

1. 완전 탐색을 시도했을 때, 여러 개의 부분 문제로 쪼개지는 구조이며 그 결과값을 재사용함으로써 큰 문제를 해결할 수 있다면.(= 점화식이 세워진다면) -> dp임.
2. d와 i를 정의한다
3. 어떤 걸 가지고 다음 i에 대한 d를 만들어낼 수 있는지를 구현한다


탑 다운 방식. 재귀 f 함수 기반 점화식
'''

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

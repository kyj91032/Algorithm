# 약수의 합 알고리즘: 자연수 n에 대하여 모든 약수의 합을 구한다

# 약수의 합 기본 동작 과정
'''
1. 1부터 sqrt(n)까지 모든 수를 확인하며
2. 약수인지(n % i == 0) 판별
3. 약수이면 sum 누적 변수에 더하기
'''

''' python

import math
def sum(n):
	s = 0
	for i in range(1, int(math.sqrt(n)) + 1): # 대칭성 활용해서 후보 제거
		if n % i == 0:
			s += i
			s += n / i
	if i * i == n:
		s -= i; # 중복
	return int(s)
'''

''' 약수의 합 아이디어 1: i를 약수로 갖는 수의 개수

n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += (n // i) * i # 어떤 자연수가 i를 약수로 가지는지는 모르지만, i를 약수로 갖는 수의 개수는 알 수 있다. (i를 약수로 갖는 수의 개수 * i = 약수 i의 합)
print(sum)
'''
''' 약수의 합 아이디어 2: 누적 dp 테이블. 1부터 배수를 추가한다.
import sys

MAX = 1000000

dp = [0] * (MAX + 1) # 각 인덱스마다 약수의 합을 담아 놓을 배열 초기화
s = [0] * (MAX + 1) # 각 인덱스까지 누적합을 담을 배열 초기화

for i in range(1, MAX + 1): # 1부터 최대값까지
    j = 1 
    while i * j <= MAX:
        dp[i * j] += i # dp 배열의 인덱스인 i의 배수에 i 값을 더해준다. 예를들면 3 * j의 해당하는 값들은 3을 무조건 약수로 가지기 때문에 3을 더해준다 
        j += 1
    s[i] = s[i - 1] + dp[i] # 해당 dp[i]의 값 까지 더한 누적합을 s배열에 넣어준다.

t = int(input())

for _ in range(t):
    a = int(sys.stdin.readline())
    sys.stdout.write(str(s[a])+"\n")
'''

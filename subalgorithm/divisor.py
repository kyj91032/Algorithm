# 약수의 합 알고리즘: 자연수 n에 대하여 모든 약수의 합을 구한다

# 약수의 합 기본 동작 과정
'''
1. n의 약수. 1부터 n까지 후보를 추리고 하나씩 약수인지 판별
2. 약수이면 sum 누적 변수에 더하기
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

''' 약수의 합 아이디어

n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += (n // i) * i # 어떤 자연수가 i를 약수로 가지는지는 모르지만, 약수 1의 합.. 2의 합.. 3의 합..으로 쭉 구할 수 있다. (i를 약수로 갖는 수의 개수 * i = 약수 i의 합)
print(sum)
'''

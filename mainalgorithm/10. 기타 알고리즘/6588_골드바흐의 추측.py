# 소수 판별 알고리즘

import sys
import math
input = sys.stdin.readline

max = 1000000 # 에라토스테네스의 체를 이용해 소수 테이블 미리 생성
array = [True for _ in range(max + 1)]
for i in range(2, int(math.sqrt(max)) + 1):
	if array[i] == True:
		j = 2
		while j * i <= max:
			array[i * j] = False
			j += 1
array[2] = False

while True:
	n = int(input())
	if n == 0:
		break
	for i in range(3, n//2 + 1, 2):
		if array[i] and array[n - i]:
			print(f"{n} = {i} + {n - i}")
			break
			
# 소수 판별 알고리즘: 자연수 n이 소수인가 아닌가를 판단하는 알고리즘.

# 소수 판별 기본 동작 과정
'''
1. 2부터 sqrt(n)까지 약수가 존재하는지(n % i == 0) 판별
'''

''' python

import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1): 
        if x % i == 0:
            return False
    return True

'''

''' n까지 모든 자연수를 소수 판별할 때 아이디어: 에라토스테네스의 체

1. 소수 판별 테이블 True로 초기화
2. 2부터 sqrt(n)까지 모든 수를 확인하며
3. i가 남은 수(소수)인 경우 i를 제외한 i의 모든 배수를 지운다

import math

n = 1000 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n + 1)] # 소수 판별 테이블 True로 초기화. 여기서 소수가 아닌 수를 지워나갈 것.

for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며 (제곱근 이전의 배수를 모두 확인하였으므로 제곱근 이후부터 n까지는 테이블이 확정된다)
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우) (소수가 남게 됨)
        j = 2 # i를 제외한 i의 모든 배수를 지우기
        while i * j <= n:
            array[i * j] = False
            j += 1
'''

# 유클리드 호제법 : 숫자 a, b가 있을 때, a를 b로 나눈 나머지와 b의 최대 공약수는 a와 b의 최대 공약수와 같다는 것을 의미한다.

# 두 수 a, b의 최소공배수 구하는 과정
'''
1. 최소공배수 구하는 lcm 함수 작성. a * b / gcd(a, b)
2. 최대공약수 구하는 gcd 함수 작성. a, b = b , a % b 계속 대입해 가고(while b > 0) 남는 a가 최대공약수
'''

''' 1934 최소공배수

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

n = int(input())

for _ in range(n):
	a, b = map(int, input().split())
	print(int(lcm(a, b))
'''

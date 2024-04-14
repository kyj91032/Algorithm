# https://boj-helper.vercel.app/solve/1010?language=python

# 생각 과정
'''
처음에 아예 감을 못잡고 문제 유형을 봄. 조합을 보고 아이디어를 얻음.
nCr을 계산하면됨. math를 이용해 공식을 계산.. 근데 다이내믹 풀이를 모르겠다

=> 이항계수의 집합(파스칼의 삼각형)이 만들어지는 것이 점화식이 존재함. -> DP
(i, j) = (i-1, j-1) + (i, j-1) 임 -> n, m에 대한 2차원 dp 테이블을 쓰면 된다
'''

# 풀이 코드 - 순열 계산
import math

T = int(input())

def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

for _ in range(T):
    n, m = map(int, input().split())

    answer = nCr(m, n)

    print(answer)

# 풀이 코드 - 파스칼의 삼각형 dp
T = int(input())

n = 30
m = 30

d = [[1] * (m+1) for _ in range(n+1)] # 1로 초기화

for i in range(2, m+1): # n이 1이면 d는 모두 m
    d[1][i] = i

# -- 양 사이드 변을 구한 상태에서 점화식 구현
for i in range(2, n+1): # n부터 차례대로 (가로)
    for j in range(i+1, m+1): # m을 돌면서 가로 내의 하나하나를 계산
        d[i][j] = d[i-1][j-1] + d[i][j-1] # m-1, n-1을 이용해 m, n이 구해짐

for _ in range(T):
    n, m = map(int, input().split())
    print(d[n][m])


# 피드백 후 정리
'''
1. 파스칼의 삼각형은 점화식(이항계수의 성질)이 있어서 다이내믹 프로그래밍으로 구현할 수 있다.
2. 2차원 dp 테이블은 표로 그리고 초기화와 점화식을 순서대로 구현한다.
'''
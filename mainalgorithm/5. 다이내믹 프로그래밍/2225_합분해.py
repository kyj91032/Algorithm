
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
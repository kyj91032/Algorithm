# https://boj-helper.vercel.app/solve/17626?language=python

# 생각 과정
'''
결국 우리는 N = (어떤 수) + (제곱 수)가 되도록 하고 싶다.
물론, 그 "어떤 수"도 제곱 수들의 합으로 이루어져 있을 것이다.
이때, 우리는 제곱 수들의 합으로 N을 표현하는데 그 제곱 수들의 개수가 최소가 되도록 해야 된다.
그렇다면 자연스럽게 dp[i] = i를 만들 때 필요로 하는 제곱 수들의 개수라고 하자.
그러면 우리는 dp[N]을 구하는 것으로 문제가 바뀌게 된다.

------------------
점화식을 못구했다..

좀 차근차근 구할 필요가 있을듯
1. dp[N] = min(dp[k]) + 1 일단 이렇게 표현하고, k는 여러개가 될 수 있다.
2. k를 식으로 표현하자면 N - (제곱수들)이므로, min(dp[N - (제곱수)]) + 1이 최종적인 식이 된다.
3. 제곱수는 일단 i보다 큰 제곱수는 필요가 없다.
4. 1~i까지 확인하면 되는데, 현재 i에서 i보다 작은 제곱수들을 뺀 값들 중 최소값을 찾고, +1을 해주면 된다.
5. 제곱수를 뺀다는 것은 모든 이전 값들을 고려하여 DP를 수행하는 것이다.
'''

# 풀이 코드
import math
 
n = int(input())
dp = [0,1]

for i in range(2, n+1):
    minValue = 1e9
    for j in range(1, int(math.sqrt(i)) + 1):
        minValue = min(minValue, dp[i - j**2]) # 
    dp.append(minValue + 1)

print(dp[n])


# 피드백 후 정리

'''
1. 점화식을 찾을때 모든 것을 고려하는 일반 식부터 쓰면서 하나씩 구체화해나가는 것이 중요하다.
2. min을 많은 범위(반복이 필요한)에서 수행할땐 for문과 같이 min을 수행할 수 있다.
'''
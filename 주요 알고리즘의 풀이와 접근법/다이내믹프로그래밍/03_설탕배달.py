# https://boj-helper.vercel.app/solve/2839?language=python

# 생각 과정
'''
만약 18kg의 무게를 구성하는 최소 개수를 구한다고 하면, 이는 18kg이전 무게값으로 구해질 수 있는 여지가 있다.
문제 상황이 이전 상황과 엮여서 완전탐색이 안되고, 이전 결과값을 재사용해야 한다.
그래서 점화식이 작성되고, dp로 풀 수 있다
i와 di를 정의한 후
d[i]가 조합되는 여러 경우 중 최소값을 구하기. -> d[i] = min(d[i-3] + 1, d[i-5] + 1) min을 활용한 점화식
'''

# 풀이 코드
n = int(input())

inf = 1e9

d = [inf] * (5001)

d[3] = 1
d[5] = 1

for i in range(7, 5001):
    d[i] = min(d[i-3] + 1, d[i-5] + 1)

answer = d[n]
if answer >= inf:
    print(-1)
else: print(answer)


# 피드백 후 정리

'''
1. 최댓값으로 초기화 할 때 inf = 1e9를 쓸 수 있다. 10의 9승(10억)
2. 문제가 완전탐색이 안되고, 이전 결과값을 활용할 수 있는 유형이다. i를 정의하고 d를 도출하는 점화식 세우기
3. d[i] = min(d[i-3] + 1, d[i-5] + 1)와 같은 min, max 함수를 활용하는 유형
'''
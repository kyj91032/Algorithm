# https://boj-helper.vercel.app/solve/1620?language=python

# 생각 과정
'''
처음엔 index를 이용해서 풀어보려고 했지만, 시간복잡도가 O(n^2)이라서 시간초과가 날 것 같아서 다른 방법을 생각함 (for x index() = n^2)
-> 인덱스와 value를 매핑한 딕셔너리를 이용해 O(1) * O(n)으로 해결할 수 있었다.
-> 핵심 아이디어는 딕셔너리를 양방향으로 두개 만드는 것이다. key, value를 서로 바꿔서 저장한다.
++ 두개 만들 필요없이 하나의 딕셔너리에 양방향 데이터를 모두 넣어도 됨.. (key, value), (value, key) 둘 다 넣어두면 됨
'''

# 풀이 코드
import sys
def input(): return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

poks = []
for _ in range(n):
    poks.append(input())

pdic1 = {}
pdic2 = {}
for idx, val in enumerate(poks):
    pdic1[idx+1] = val
    pdic2[val] = idx+1

answer = []
for _ in range(m):
    s = input()
    if s.isdigit():
        answer.append(pdic1[int(s)])
    else:
        answer.append(pdic2[s])

for e in answer:
    print(e)

# 피드백 후 정리
'''
1. 어떤 문자열이 정수로 이루어져 있는지 확인하는 방법은 isdigit()을 사용한다.
2. 특정 값에 대한 인덱스가 묶여있는 경우 딕셔너리를 생각한다. 딕셔너리는 key에 따른 value값을 찾는데에 O(1)이므로 시간복잡도에서 유리하다.
3. n이 100,000쯤 되는데 n^2의 시간복잡도가 나오면 map(in 연산자, 딕셔너리, hash함수 등) 을 의심해볼만하다.
'''
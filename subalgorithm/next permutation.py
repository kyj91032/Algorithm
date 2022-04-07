# 다음 순열 알고리즘: 순열 및 조합을 생성할 때 재귀적으로 구현하지 않고 각 인덱스 값을 비교하여 모든 경우의 인덱스 값을 뽑아내는 방법(BF). 현 순열에서 사전 순(오름차순)으로 다음 순열을 리턴한다.

# 다음 순열 기본 동작 과정
'''
1. 뒤에서부터 탐색하면서 오름차순이 깨지는 인덱스를 확인(a)
2. 다시 뒤에서부터 탐색하면서 a보다 큰 첫번째 인덱스를 확인(b)
3. a와 b를 스왑
4. a + 1 에서부터 끝까지를 오름차순 정렬
'''

'''

import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))

x = 0
for i in range(n - 1, 0, -1):
    if s[i - 1] < s[i]:
        x = i - 1
        break
for i in range(n - 1, 0, -1):
    if s[x] < s[i]:
        s[x], s[i] = s[i], s[x]
        s = s[:x + 1] + sorted(s[x + 1:])
        print(*s)
        exit()
print(-1)
'''

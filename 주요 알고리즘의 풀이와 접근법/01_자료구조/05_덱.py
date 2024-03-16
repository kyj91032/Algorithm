# https://boj-helper.vercel.app/solve/10866?language=python

# 생각 과정
'''
덱 구현이라서 바로 deque로 구현했다
'''

# 풀이 코드
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

dque = deque()
for _ in range(n):
    s = list(input().split())
    if s[0] == 'push_front':
        dque.appendleft(s[1])
    if s[0] == 'push_back':
        dque.append(s[1])
    if s[0] == 'pop_front':
        if dque:
            print(dque.popleft())
        else:
            print(-1)
    if s[0] == 'pop_back':
        if dque:
            print(dque.pop())
        else:
            print(-1)
    if s[0] == 'size':
        print(len(dque))
    if s[0] == 'empty':
        if dque:
            print(0)
        else:
            print(1)
    if s[0] == 'front':
        if dque:
            print(dque[0])
        else:
            print(-1)
    if s[0] == 'back':
        if dque:
            print(dque[-1])
        else:
            print(-1)


# 피드백 후 정리
'''
deque는 맨 앞쪽에서 appendleft, popleft, 맨 뒤쪽에서 append, pop을 할 수 있다.
'''
# https://boj-helper.vercel.app/solve/18258?language=python

# 생각 과정
'''
00_스택 문제와 비슷한 문제이다. 스택을 큐로 바꾸면 된다.
파이썬에선 큐를 deque로 구현하면 된다.
queue 선언을 for문 안에서 해버려서 틀렸다. for문 안에서 해버리면 for문이 돌 때마다 queue가 초기화되기 때문이다...
'''

# 풀이 코드
from collections import deque

T = int(input())
queue = deque()

for _ in range(T):

    s = list(input().split())
    
    if s[0] == 'push':
        queue.append(s[1])
    if s[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    if s[0]=='size':
        print(len(queue))
    if s[0]=='empty':
        if len(queue)==0:
            print(1)
        else: print(0)
    if s[0]=='front':
        if len(queue) == 0:
            print(-1)
        else: print(queue[0])
    if s[0]=='back':
        if len(queue) == 0:
            print(-1)
        else: print(queue[-1])
    


# 피드백 후 정리
'''
주어진 테스트 케이스를 잘 보자.
이번 문제는 여러 테스트 케이스가 아니라 한 테스트 케이스에서 여러 명령어를 for문으로 실행하는 것이다.
그래서 queue 선언을 for문 밖에서 먼저 한 후 for문을 돌려야 한다.
'''
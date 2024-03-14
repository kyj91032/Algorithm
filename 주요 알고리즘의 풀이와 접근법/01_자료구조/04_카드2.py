# https://boj-helper.vercel.app/solve/2164?language=python

# 생각 과정
'''
맨 앞을 빼고 맨 뒤로 보낸다 -> 바로 큐 자료구조가 떠올랐다.
popleft와 append를 사용하면 됐다.
'''

# 풀이 코드
from collections import deque

N = int(input())

queue = deque([i for i in range(1, N+1)])

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])

# 피드백 후 정리

'''
선입선출 -> 큐 자료구조를 사용
'''
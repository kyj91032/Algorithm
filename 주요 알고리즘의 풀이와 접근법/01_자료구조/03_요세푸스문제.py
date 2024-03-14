# https://boj-helper.vercel.app/solve/1158?language=python

# 생각 과정
'''
1~N까지를 리스트로 정의하고, K번째 원소를 빼내는 것을 반복하면 된다고 생각했다.
하지만 반복문을 돌면서 리스트의 원소를 빼내면 리스트의 길이가 줄어들기 때문에 구현이 어려웠다.
그래서 큐를 사용하면 될까 생각했다.
그래도 리스트로 구현하는 것과 다를 바 없었다.

해답
=> deque.rotate()를 사용하면 됐다. rotate()는 인자로 받은 수만큼 원소를 회전시킨다.

'''


# 풀이 코드

from collections import deque

n, k = map(int, input().split())

queue = deque([i for i in range(1, n+1)])
result = []

while len(queue) > 0:
    queue.rotate(-(k-1))
    result.append(queue.popleft())

print('<'+', '.join(map(str, result))+'>')


# 피드백 후 정리

'''
파이썬의 deque는 스택, 큐, 덱 뿐만 아니라 rotate()를 사용하면 원형 큐도 구현할 수 있다.
deque.rotate()는 인자로 받은 수만큼 원소를 회전시킨다.
rotate를 한 뒤 popleft나 pop을 하면 원형 큐에서의 입출력을 구현하는 것이다.
'''
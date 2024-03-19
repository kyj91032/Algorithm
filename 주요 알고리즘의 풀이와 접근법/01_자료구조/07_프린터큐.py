# https://boj-helper.vercel.app/solve/1966?language=python

# 생각 과정
'''
문제에서 que 명시 -> deque 사용
값이 몇 번째인지를 알아야했기 때문에 딕셔너리를 생각했었는데, 이걸 큐에 넣어서 돌려야하니까 결국 딕셔너리보다 인덱스를 가지는 이중리스트를 이용해야겠다고 생각했다
이중 리스트에서 max값을 찾는데에 리스트 컴프리헨션을 사용했다. sorted의 lambda처럼 쓸수있을까 했는데 안됐다.
que는 가변이기 때문에 for문이 아니라 while que:로 돌려야하는 걸 알고있었다.
'''

# 풀이 코드
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    result = []
    que = deque()
    li = list(map(int, input().split()))
    for key, value in enumerate(li):
        que.append([key, value])

    while que:
        if que[0][1] == max(q[1] for q in que):
            result.append(que.popleft())
        else:
            que.append(que.popleft())
    
    for i in range(len(result)):
        if result[i][0] == m:
            print(i+1)
            break


# 피드백 후 정리

'''
1. que를 순회하는 방법은 for문이 아닌 while que: 이다
2. 이중 리스트에서 최댓값은 리스트 컴프리헨션을 사용해서 찾을 수 있다. max(q[1] for q in que)
3. enumerate를 사용해서 인덱스를 가지는 이중리스트를 만들 수 있다. 이것과 딕셔너리 중 어떤 것을 사용할지 고민해보기
    이 문제의 경우 que를 돌려야해서 딕셔너리보다는 이중리스트가 더 편했다. 결국 큐에는 iteratble한 객체만 들어갈 수 있기 때문에 딕셔너리를 큐에 넣을 수 없었다.
'''
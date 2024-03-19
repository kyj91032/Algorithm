# https://boj-helper.vercel.app/solve/2346?language=python

# 생각 과정
'''
07번 문제에서 큐 안에 enumerate를 이용해 인덱스를 같이 넣어서 풀었던 것을 떠올렸다. 딕셔너리는 필요없는 경우다.

rotate의 회전 방향과 회전 수를 헷갈렸다.
예시로 해보면서 rotate의 방향과 회전 수를 정확히 이해했다.
'''

# 풀이 코드
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

li = list(map(int, input().split()))

que = deque()
for key, value in enumerate(li):
    que.append([key+1, value])
result = []
while que:
    elem = que.popleft()
    result.append(elem[0])
    if elem[1] > 0:
        que.rotate(-(elem[1]-1)) 
        # 여기가 -1인 이유는 
        # k가 음수인 경우는 큐의 맨 앞 원소가 맨 뒤로 움직이기 때문에 
        # 이전에 맨 앞 원소를 pop한 것을 고려해서 -1을 해줘야 한다.(덜 옮기기)
    elif elem[1] < 0:
        que.rotate(-elem[1])
        # 여기서 -1을 안해주는 이유는
        # k가 양수인 경우는 큐의 맨 뒤 원소가 맨 앞으로 움직이기 때문에
        # 맨 앞 원소를 pop한 것을 고려하지 않아도 된다
    
print(' '.join(map(str,result)))

# 피드백 후 정리

'''
1. deque의 rotate()는 인자로 받은 수만큼 원소를 회전시킨다.
하지만 k가 양수일 때는 맨 뒤 원소가 맨 앞으로 이동하고,
k가 음수일 때는 맨 앞 원소가 맨 뒤로 이동한다.

que = deque([1,2,3,4,5])
que.rotate(3)
print(que) -> deque([3, 4, 5, 1, 2])
que.rotate(-3)
print(que) -> deque([1, 2, 3, 4, 5])
'''
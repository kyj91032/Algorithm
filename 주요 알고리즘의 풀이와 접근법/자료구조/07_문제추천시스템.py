# https://boj-helper.vercel.app/solve/21939?language=python

# 생각 과정
'''
solved에 들어간 것 (큐에서 삭제해야하는것 )을 어떻게 반영해야하는지를 명확히 해야하는 문제였다.
'''

# 풀이 코드
import sys
import heapq
from collections import defaultdict

def input(): return sys.stdin.readline().rstrip()

min_heap = []
max_heap = []
solved = defaultdict(int) # 존재하지 않는 키에 대해서 기본값 0으로 줌
n = int(input())

for _ in range(n):
    p, l = map(int, input().split())
    # 난이도 순이 먼저라서 l을 먼저 씀
    heapq.heappush(min_heap, (l, p)) # 최소 큐 초기화
    heapq.heappush(max_heap, (-l, -p)) # 최대 큐 초기화

m = int(input())
for _ in range(m):
    cmd = input().split() # 명령 받음
    # 추천 시 동기화가 돼있어야 제대로 추천이 가능함 -> 삭제시에 동기화
    if cmd[0] == 'recommend':
        if cmd[1] == '1': # 어려운 문제 출력 -> 최대 힙에서 출력
            print(-max_heap[0][1]) # 최대 힙에서 출력 - 최대값 기준은 그대로 l -> p 순서이고 출력만 번호만 출력하는 거임. 난이도 제일 높은거의 번호만 출력하는 것
        else: # 쉬운 문제 출력
            print(min_heap[0][1])
    
    # 추가 시 동기화 필요 X 둘다 그냥 추가하면 됨
    elif cmd[0] == 'add':
        p = int(cmd[1])
        l = int(cmd[2])
        heapq.heappush(min_heap, (l, p)) # 최소 큐에 추가
        heapq.heappush(max_heap, (-l, -p)) # 최대 큐에 추가
    
    # 삭제 시 동기화가 필요. 둘다 삭제를 못함. 최소큐 vs 최대큐 충돌
    elif cmd[0] == 'solved':
        # 공유 공간에서 푼 문제 기록
        solved[int(cmd[1])] += 1 # 푼 문제 추가 - 문제 번호와 개수로 매핑

        # 최대 힙 동기화
        while solved[abs(max_heap[0][1])] != 0: # solved에 푼 문제가 있으면 -> 문제 번호에 매핑된 개수가 0이 아니면 -> 최대 큐에 반영
            solved[abs(max_heap[0][1])] -= 1 # 푼 문제 개수를 1 줄임
            heapq.heappop(max_heap) # 최대 힙에서 삭제
        # 최소 힙 동기화
        while solved[min_heap[0][1]] != 0: # solved에 푼 문제가 있으면 -> 문제 번호에 매핑된 개수가 0이 아니면 -> 최소 큐에 반영
            solved[min_heap[0][1]] -= 1
            heapq.heappop(min_heap)

# 피드백 후 정리

'''
1. solved에 푼 문제를 기록하고, solved에 푼 문제가 있으면 최대 힙, 최소 힙에서 삭제를 해줌
2. 현재 최대큐, 최소큐에 해당하는 top 값이 solved에 있으면(= dict에 개수 >= 1), dict -= 1 해주고, heap에서도 삭제 해줌
'''
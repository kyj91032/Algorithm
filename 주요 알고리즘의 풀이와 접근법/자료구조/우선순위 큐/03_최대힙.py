# https://boj-helper.vercel.app/solve/11279?language=python

# 생각 과정
'''
일반적인 리스트에서 max를 계속 쓰면서 최댓값을 찾을 수 있지만, 우선순위 큐를 이용해 최댓값을 빠르게 연속적으로 뺄 수 있다.
'''

# 풀이 코드
import sys
import heapq

def input(): return sys.stdin.readline().rstrip()

n = int(input())

pq = [] # priority queue

for _ in range(n):
    k = int(input())
    if k != 0:
        heapq.heappush(pq, -k) # 최대힙을 만들기 위해 음수로 넣어줌
    else:
        if pq:
            print(-heapq.heappop(pq)) # 최대힙이므로 다시 양수로 출력
        else:
            print(0)


# 절댓값 힙
import sys
import heapq

def input(): return sys.stdin.readline().rstrip()

pq = []

n = int(input())

for i in range(n):
    k = int(input())
    if k == 0:
        if pq:
            print(heapq.heappop(pq)[1])
        else:
            print(0)
    elif k < 0:
        heapq.heappush(pq, (-k, k)) # 처음엔 절댓값을 기준으로 pop하고, 그 다음엔 원래 값을 기준으로 pop하기 위해
        # (절댓값, 원래값) 순서로 튜플로 넣어줌. 그리고 출력할땐 원래값 ([1])을 출력함.
    else:
        heapq.heappush(pq, (k, k))


# 피드백 후 정리
'''
1. 파이썬에서 우선순위 큐는 heapq를 사용한다.
    import heapq
    pq = []
    heapq.heappush(pq, 4)
    min_val = heapq.heappop(pq) # 최소 큐
    
    heapq.heappush(pq, -4)
    max_val = -heapq.heappop(pq) # 최대 큐

2. 리스트에서 최댓값을 찾는 것과 우선순위 큐에서 최댓값을 찾는 것의 시간복잡도 차이
    리스트: O(n)
    우선순위 큐: O(logn)

3. 우선순위 큐는 튜플의 첫번째 값, 두번째 값, 순서대로 정렬에 고려된다.

'''
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
    리스트: O(n)을 반복
    우선순위 큐: O(logn)을 반복
'''
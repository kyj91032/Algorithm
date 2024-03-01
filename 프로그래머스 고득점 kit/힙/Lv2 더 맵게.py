'''
https://school.programmers.co.kr/learn/courses/30/lessons/42626

1. 리스트로 접근
2. 값을 넣을 때마다 정렬을 해야함
3. 리스트 -> 힙으로 변경
4. 힙으로 변경하면서 최소값을 뽑아내는 것, 정렬하는 것이 자연스럽게 이루어짐
'''

import heapq

def solution(S, K):
    heap = [] # 일반 리스트 선언
    for i in S:
        heapq.heappush(heap, i) # 힙 연산. s의 모든 값을 힙에 넣으면서 자동 정렬

    cnt = 0
    while heap[0] < K: # 최소값이 K보다 작은 동안만 수행. 커지면 cnt 리턴
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2) 
        # 최소값 2개를 뽑아서(알아서 remove됨) 연산 후 다시 힙에 넣기 -> 자동 정렬
        cnt += 1 # 연산 횟수 카운트
        
        if len(heap) == 1 and heap[0] < K: # 연산 후 남은 값이 1개이고, 그 값이 K보다 작다면
            return -1
    return cnt

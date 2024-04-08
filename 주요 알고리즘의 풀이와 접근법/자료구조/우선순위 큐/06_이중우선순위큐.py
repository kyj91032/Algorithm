# https://boj-helper.vercel.app/solve/7662?language=python

# 생각 과정
'''
최대 힙과 최소 힙을 어떻게 동시에 쓸 수 있을까 생각했다. 힙을 두개 둬서 해보려고 했는데 실패했다. 둘을 동기화를 못시켰다.

=> 값의 추가와 삭제를 공통으로 기록하는 공간을 활용해야 했다..
-> 값의 추가와 삭제를 O(1)으로 할 수 있는 dict를 활용
모든 추가와 삭제 시 dict에 반영하면서 최대 힙과 최소 힙을 동기화 시킬 수 있다.
dict는 value:number로 저장.
-> 대신에 진짜 최대 힙, 최소 힙에서 가짜 값(개수가 0인 값)을 매번 확인해줘야함. heap에는 덜 반영되어있기 때문에
-> 덜 반영되는 이유는 최대 힙에서 삭제된 값이 최소 힙에 반영되지 않고, 최소 힙에서 삭제된 값이 최대 힙에 반영되지 않기 때문

'''

# 풀이 코드
import sys
import heapq

def input(): return sys.stdin.readline().rstrip()

def isEmpty(nums): # 큐에 값이 있는지 확인
    for item in nums:
        if item[1] > 0:
            return False
    return True

T = int(input())

for _ in range(T):
    pq_min = [] # 최소 힙
    pq_max = [] # 최대 힙
    nums = dict() # 값의 추가 삭제를 두 힙 모두에 반영하기 위한 공간. 값의 모든 추가, 삭제를 반영함.
    n = int(input())
    for i in range(n):
        op, value = input().split()
        value = int(value)
        if op == 'I':
            if value in nums:
                nums[value] += 1 # 중복 값 삽입의 경우
            else:
                nums[value] = 1 # 최초 삽입의 경우
                heapq.heappush(pq_min, value)
                heapq.heappush(pq_max, -value)
        else: # op == 'D'
            if not isEmpty(nums.items()): # 큐가 비어있는 지 여부를 큐를 각각 확인하는게 아니라 공통 공간인 nums를 확인
                if value == 1: # 최대 큐
                    while -pq_max[0] not in nums or nums[-pq_max[0]] < 1:
                        # 최대 큐의 최대값이 nums에 없거나, 그 값의 개수가 0이면. 실제론 삭제되었지만 각각의 힙에는 반영되지 않은 것. 그래서 삭제해줘야함
                        pop = -heapq.heappop(pq_max)
                        if pop in nums:
                            del(nums[pop]) # 딕셔너리 값 삭제
                    nums[-pq_max[0]] -= 1
                else:
                    while pq_min[0] not in nums or nums[pq_min[0]] < 1:
                        pop = heapq.heappop(pq_min)
                        if pop in nums:
                            del(nums[pop])
                    nums[pq_min[0]] -= 1
    if isEmpty(nums.items()): # 큐가 비어있는 경우
        print('EMPTY')
    else:
        while -pq_max[0] not in nums or nums[-pq_max[0]] < 1: # 가짜 값 제거
            heapq.heappop(pq_max) # 최대값 출력
        while pq_min[0] not in nums or nums[pq_min[0]] < 1: # 가짜 값 제거
            heapq.heappop(pq_min) # 최소값 출력
        print(-pq_max[0], pq_min[0])

# 피드백 후 정리

'''
1. 어떤 값(종류)에 따른 개수가 매핑되면 딕셔너리를 이용하기, + 종류먄 필요하다면 집합을 이용
2. 디테일한 구현은 틀부터 구현하고 테스트 케이스를 돌리면서 구체적인 구현을 해나가는 것이 좋다.
'''
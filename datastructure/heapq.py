# 힙 정렬: 힙이라는 자료구조를 이용한 정렬 방법. heap기능을 위해 heapq 라이브러리를 사용한다.


import heapq
# heapq는 우선순위 큐를 구현하고자 할 때 사용하며 파이썬의 힙은 최소 힙으로 구성되어 있으므로 원소를 힙에 넣었다가 뺀느 것만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬이 완료된다. 원소를 삽입할 때는 heapq.heappush(), 꺼낼 때는 heapq.heappop()을 이용한다.

def heapsort(iterable):
  h = [] # 우선순위 큐 공간 생성
  result = []
  for value in iterable:
    heapq.heappush(h, value) # 삽입
  for _ in range(len(h));
    result.append(heapq.heappop(h)) # 추출
  return result

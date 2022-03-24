''' 파이썬에서 queue
from collections import deque  # queue 라이브러리보다 효율적이고 간단해서 그냥 deque 씀
queue = deque()  # 큐 구현을 위해 deque 라이브러리 사용. 큐 공간 생성. queue를 deque 객체로 정의. deque([list]) 리스트를 매개변수로 받아서 시작 데이터 설정 가능.
삽입5 - 삽입2 - 삽입3 - 삽입7 - 삭제 - 삽입1 - 삽입4 - 삭제
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()  # 덱의 왼쪽에서 데이터 삭제
queue.append(1)
queue.append(4)
queue.popleft()
print(queue)  # 먼저 들어온 순서대로 출력.
deque([3, 7, 1, 4])  # 리스트로 변환하려면 list().


'''

# 맨 앞 원소보다 작은 원소가 나올 때까지 시간을 증가시키고, 작은 원소가 나오면 그 시간을 리스트에 추가한다.
# 맨 앞 원소를 pop 하는 아이디어 -> deque를 사용하면 된다.

from collections import deque

def solution(prices):

    answer = []
    ps = deque(prices)

    while ps:
        time = 0
        p = ps.popleft()
        if len(ps) == 0:
            answer.append(0)
            break
        for i in ps:
            time += 1
            if p > i:
                break
        answer.append(time)

    return answer # 반환은 deque이 아닌 list로 해야함
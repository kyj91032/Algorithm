
# 14501 퇴사

import sys
input = sys.stdin.readline

n = int(input())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))

M = 0

def go(day, total):
    global M
    if day == n:  # n에 알맞게 도착했을 때, 정답이 될 수 있다. # 깊이에 따른 종료조건.
        M = max(M, total)
        return
    if day > n:  # n을 초과한다면 범위 안에 일을 못끝내므로, 정답이 될 수 없다. # 깊이에 따른 종료조건
        return
    go(day + 1, total) # 이번 day는 일을 하지 않고 그냥 넘어간다!
    go(day + s[day][0], total + s[day][1]) # 이번 day일을 처리한다, 기간도 점프한다! # 모든 경우 재귀 호출해서 M값 최신화하기 (최대최소 bf + 재귀적 구현)

go(0, 0) # day는 0, total도 0부터 시작.
print(M)


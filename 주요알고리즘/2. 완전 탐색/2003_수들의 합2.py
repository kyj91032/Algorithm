import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = list(map(int, input().split()))

p1 = 0
p2 = 0
cnt = 0

# 이중 반복문을 사용하면 시간초과가 난다.
# 부분 합이 큰 경우에는 p1을 증가시켜야 하고, 작은 경우에는 p2를 증가시키는 투포인터 방식으로 구현하여 완전탐색의 시간복잡도를 줄이는 문제
# 필요없는 탐색을 찾아내고 줄이는 것이 핵심

while p2 <= n and p1 <= p2:
    if sum(a[p1:p2]) == m:
        cnt += 1
        p1 += 1
    elif sum(a[p1:p2]) > m:
        p1 += 1
    else:
        p2 += 1

print(cnt)
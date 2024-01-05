
# 15656 n과 m (7) - 리스트의 원소 중에 중복 순열 (재귀를 이용한 완전 탐색. 백트래킹x)

n, m = map(int, input().split())
list = list(map(int, input().split()))

list.sort()

s = []

def rec(): # bruteforce 인데 반복으로 안되서 재귀로 접근.
    if len(s) == m: # 종료 조건
        print(' '.join(map(str, s)))
        return
    
    for i in list: # 완전 탐색
        s.append(i)
        rec() # 재귀 호출
        s.pop()
rec()


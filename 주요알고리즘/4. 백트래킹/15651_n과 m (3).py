

# 15651 n과 m (3) - 1부터 n까지 중에 중복 순열 (완전 탐색의 재귀적 구현 recursive bruteforce, 가지치기 없음)

n, m = list(map(int, input().split()))

s = []

def rec(): # bruteforce 인데 반복으로 안되서 재귀로 접근.
    if len(s) == m: # 종료 조건
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1): # 완전 탐색
        s.append(i)
        rec() # 재귀 호출
        s.pop()
rec()


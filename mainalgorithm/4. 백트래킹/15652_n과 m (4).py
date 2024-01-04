

# 15652 n과 m (4) - 1부터 n까지 중에 비내림차순 순열

n, m = list(map(int, input().split()))
 
s = []

def rec(start): # bruteforce 인데 반복으로 안되서 재귀로 접근.
    if len(s) == m: # 종료 조건
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n + 1): # 완전 탐색
        # 비내림차순을 구현하기 위해 중복 제거 가지치기는 없애야 함.
        s.append(i)
        rec(i) # 재귀 호출. 비 내림차순이므로 rec(i + 1)이 아닌 rec(i)로 호출
        s.pop()
rec(1)

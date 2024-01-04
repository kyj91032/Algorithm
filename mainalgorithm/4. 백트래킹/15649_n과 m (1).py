
# 15649 n과 m (1) - 1부터 n까지 중에 순열

n, m = list(map(int, input().split()))
 
s = []

def rec(): # bruteforce 인데 반복으로 안돼서 재귀로 접근.
    if len(s) == m: # 종료 조건. 이 깊이에서는 재귀를 할 필요가 없는 것
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1): # 완전 탐색
        if i not in s: # 가지치기 구현. if 만족할때만 재귀.
            s.append(i) # 나아가기
            rec() # 재귀 호출
            s.pop() # 돌아가기
rec()

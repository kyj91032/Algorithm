

# 15650 n과 m (2) - 1부터 n까지 중에 오름차순 순열

n, m = list(map(int, input().split()))

s = []

def rec(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n + 1): # 오름차순 조건을 고려하여 현재 숫자(start) 보다 높게 가지치기
        if i not in s:
            s.append(i)
            rec(i + 1)
            s.pop()
rec(1)


# 백트래킹: 답이 이미 아닌 곳은 탐색을 하지 않고 가지치기 하는 것.

# 백트래킹의 기본 동작 과정
'''
1. 재귀함수를 정의한다.
2. 재귀 조건을 설정하여 반복하는데, 여기서 가지치기를 구현해야 한다.
'''

''' n과 m (2)

n, m = list(map(int, input().split()))

s = []

def rec(start): 
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n + 1):
        if i not in s:
            s.append(i)
            rec(i + 1)
            s.pop()
dfs(1)
'''


'''

'''

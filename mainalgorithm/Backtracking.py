# 백트래킹: 

# 백트래킹의 기본 동작 과정
'''
1. 
'''

''' n과 m (1)

n, m = list(map(int, input().split()))
 
s = []
 
def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()
'''


''' n과 m (2)

n, m = list(map(int, input().split()))

s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n + 1):
        if i not in s:
            s.append(i)
            dfs(i + 1)
            s.pop()
dfs(1)
'''

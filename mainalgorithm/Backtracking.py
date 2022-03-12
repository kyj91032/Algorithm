# 백트래킹: 완전 탐색(brute force)을 재귀적(recursive)으로 수행했을 때, 가지치기를 활용하여 시간복잡도를 줄이는 것을 백트래킹(back tracking)이라고 한다. (In the first place, DFS is about graph..)

# 백트래킹의 기본 동작 과정
'''
1. 재귀함수를 정의한다.
2. 재귀 조건을 설정하여 반복하는데, 여기서 가지치기를 구현해야 한다.
'''

''' n과 m (1)

n, m = list(map(int, input().split()))
 
s = [] # 재귀 조건을 설정하는 과정에서 스택이 필요해서 정의.

def rec(): # BF, 반복 안되서 재귀로 접근.
    if len(s) == m: # 재귀 조건 1. (m의 값 조건 고려)
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1):
        if i not in s: # i가 s에 없으면, 재귀 조건 2. (중복 안되는 조건 고려) 
            s.append(i) # push
            rec() # 재귀 호출
            s.pop() # 종료 호출 시 pop하고 다음 i로 반복을 통해 가지치기 구현
rec()
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

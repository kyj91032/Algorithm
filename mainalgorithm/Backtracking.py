# 백트래킹: 완전 탐색(brute force)을 재귀적(recursive)으로 수행했을 때, 가지치기를 활용하여 시간복잡도를 줄이는 것을 백트래킹(back tracking)이라고 한다.
# (In the first place, DFS is about graph..)

# 백트래킹의 기본 동작 과정
'''
1. 재귀함수를 정의한다.
2. 재귀 조건을 설정하여 반복하는데, 여기서 가지치기를 구현해야 한다.
'''

''' n과 m (1)

n, m = list(map(int, input().split()))
 
s = []

def rec(): # bruteforce 인데 반복으로 안되서 재귀로 접근.
    if len(s) == m: # 종료 조건
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1): # 완전 탐색
        if i not in s: # 가지치기 구현. 처음에 111 112 113 121 122 123 131 .. 이렇게 가는 건 단순 bf인데,
                       # 여기서 중복제거 조건을 고려하니 123 124 132 134 142 143 으로 출력해야 하는 거였고, 결국 중복 제거 조건의 삽입이 가지치기를 구현한 것이 되었다.
            s.append(i)
            rec() # 재귀 호출
            s.pop()
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

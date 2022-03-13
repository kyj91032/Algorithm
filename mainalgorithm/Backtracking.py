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
    
    for i in range(start, n + 1): # 오름차순 조건을 고려하여 현재 숫자(start) 보다 높게 가지치기
        if i not in s:
            s.append(i)
            rec(i + 1)
            s.pop()
rec(1)
'''


''' n과 m (3) (완전 탐색의 재귀적 구현 recursive bruteforce, 가지치기 없음)

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
'''


''' n과 m (4)

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
'''


''' n과 m (5)

n, m = map(int, input().split())
list = list(map(int, input().split()))

list.sort() # 정렬된 리스트 추가

s = []

def rec(): # bruteforce 인데 반복으로 안되서 재귀로 접근.
    if len(s) == m: # 종료 조건
        print(' '.join(map(str, s)))
        return
    
    for i in list: # 리스트에서 완전 탐색
        if i not in s: # 가지치기 구현. 처음에 111 112 113 121 122 123 131 .. 이렇게 가는 건 단순 bf인데,
                       # 여기서 중복제거 조건을 고려하니 123 124 132 134 142 143 으로 출력해야 하는 거였고, 결국 중복 제거 조건의 삽입이 가지치기를 구현한 것이 되었다.
            s.append(i)
            rec() # 재귀 호출
            s.pop()
rec()
'''


''' n과 m (6)

n, m = map(int, input().split())
list = list(map(int, input().split()))

list.sort()

s = []

def rec(start): # bruteforce 인데 반복으로 안되서 재귀로 접근.
    if len(s) == m: # 종료 조건
        print(' '.join(map(str, s)))
        return
    
    for i in list[start:]: # 완전 탐색. 오름차순 조건을 고려하여 현재 숫자(list[start]) 보다 높게 가지치기
        if i not in s: # 가지치기 구현. 처음에 111 112 113 121 122 123 131 .. 이렇게 가는 건 단순 bf인데,
                       # 여기서 중복제거 조건을 고려하니 123 124 132 134 142 143 으로 출력해야 하는 거였고, 결국 중복 제거 조건의 삽입이 가지치기를 구현한 것이 되었다.
            s.append(i)
            rec(list.index(i) + 1) # 재귀 호출
            s.pop()
rec(0)
'''


''' n과 m (7) 재귀를 이용한 완전 탐색. 백트래킹x

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
'''


''' n과 m (8)

n, m = map(int, input().split())
list = list(map(int, input().split()))

list.sort()

s = []

def rec(start): # bruteforce 인데 반복으로 안되서 재귀로 접근.
    if len(s) == m: # 종료 조건
        print(' '.join(map(str, s)))
        return
    
    for i in list[start:]: # 완전 탐색. 비내림차순이므로 list[start]부터 시작
        # 비내림차순을 위해 중복 제거 조건은 없앤다.
        s.append(i)
        rec(list.index(i)) # 재귀 호출. 비내림차순이므로 list.index(i) + 1이 아닌 list.index(i)로 호출
        s.pop()
rec(0)
'''



# 백트래킹: 완전 탐색(brute force)을 재귀적(recursive)으로 수행했을 때, 가지치기를 활용하여 시간복잡도를 줄이는 것을 백트래킹(back tracking)이라고 한다.
# (In the first place, DFS is about graph..)

# 백트래킹의 기본 동작 과정
'''
1. 재귀함수를 정의한다.
2. 기본적으로 BF를 재귀적으로 수행하려 할 때 필요한 것이 깊이에 따른 종료 조건이고,
3. 여기서 백트래킹을 하려면 완전 탐색 중에 다른 재귀 조건을 추가하여 가지치기를 구현해야한다.
'''

''' n과 m (1)

n, m = list(map(int, input().split()))
 
s = []

def rec(): # bruteforce 인데 반복으로 안되서 재귀로 접근.
    if len(s) == m: # 필수 종료 조건
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


''' nm과 k (1)

def dfs(x, y, cnt, sum_value): # 재귀함수 정의
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)] # 탐색에 이용할 방향 정의
    if cnt == k: # 깊이에 따른 종료 조건
        global max_value
        max_value = max(max_value, sum_value) # 최댓값 갱신
        return
    for i in range(x, n): # 현재 줄 부터 탐색
        for j in range(y if i == x else 0, m): # 처음엔 y부터 m까지, 다음엔 0부터 m 까지 탐색
            if check[i][j]: # 현재 노드 방문 했다면 가지치기
                continue
            around = True
            for dx, dy in dxy: # 인접 노드 방문 했다면 가지치기
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m and check[nx][ny]:
                    around = False
                    break
            if around: # 방문하기
                around = 0
                check[i][j] = True
                dfs(i, j, cnt + 1, sum_value + item[i][j]) # 재귀 호출
                check[i][j] = False

n, m, k = map(int, input().split())
item = []
for _ in range(n):
    item.append(list(map(int, input().split())))

max_value = 0 # 최댓값 초기값
check = [[False for _ in range(m)] for _ in range(n)] # 방문 여부 테이블
dfs(0, 0, 0, 0)
print(max_value)
'''


''' 1759 암호 만들기 - 백트래킹

l, c = map(int, input().split())
cl = list(input().split())

cl.sort()

mo = ['a', 'e', 'i', 'o', 'u'] # 모음 테이블. if in으로 모음인지 바로 판단 가능

s = []

def rec(start):
	if len(s) == l:
		m = 0
		n = 0
		for j in range(len(s)):
			if s[j] in mo: # 모음이면 출력하기
				m += 1
			else: n += 1
		if n >= 2 and m >= 1:
			print(''.join(map(str, s)))
			return
		else:
			return
  
	for i in cl[start:]:
		if i not in s:
			s.append(i)
			rec(cl.index(i) + 1)
			s.pop()
rec(0)
'''


''' 14889 스타트와 링크

from itertools import combinations

n = int(input())

s = [] #input

for _ in range(n):
	s.append(list(map(int, input().split())))

t = [] # rec stack
m = []

def rec(start):
	if len(t) == int(n/2):
		sum = 0
		c = list(combinations(t, 2)) # 리스트 t에서 조합 
		for k in c:
			sum += s[k[0] - 1][k[1] - 1] + s[k[1] - 1][k[0] - 1]
		m.append(sum)
		return
	
	for i in range(start, n + 1):
		t.append(i)
		rec(i + 1)
		t.pop()
rec(1)

m2 = []
l = len(m)

for j in range(int(l/2)):
	m2.append(abs(m[j] - m[l - 1 - j]))

print(min(m2))
'''


''' 15661 링크와 스타트

from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input())

s = [] # input

for _ in range(n):
	s.append(list(map(int, input().split())))


t = [] # recstack
m = []


def rec(start, k):
	if len(t) == k:
		if k == 1:
			m.append(0)
		else:
			sum = 0
			c = list(combinations(t, 2))
			for k in c:
				sum += s[k[0] - 1][k[1] - 1] + s[k[1] - 1][k[0] - 1]
			m.append(sum)
		return
		
	for i in range(start, n + 1):
		t.append(i)
		rec(i + 1, k)
		t.pop()

for p in range(1, n):
	rec(1, p)

m2 = []
l = len(m)

for j in range(int(l/2)):
	m2.append(abs(m[j] - m[l - 1 - j]))

print(min(m2))
'''

# 집합 자료구조: 수학에서의 집합과 같은 자료구조

# 집합의 기본 동작 과정

1. 집합 공간을 정의한다.
2. 집합 공간에서 add와 discard를 수행한다.


# set 코드

# 11723 집합 - 파이썬 set() 이용
import sys

s = set()
n = int(input())

for i in range(n):
	tmp = sys.stdin.readline().strip().split() # strip 왜? 쌩으로 받은거라 \n같은거 없애려고
	
	if len(tmp) == 1: # all, empty인 경우 바로 처리
		if tmp[0] == 'all':
			s = set([i for i in range(1, 21)])
		else:
			s = set()
		continue
	
	command, target = tmp[0], tmp[1]
	target = int(target)
	
	if command == 'add': # 집합에 원소 추가. add함수
		s.add(target)
	elif command == 'check':
		print(1 if target in s else 0)
	elif command == 'remove': # 집합에 원소 삭제. discard함수
		s.discard(target)
	elif command == 'toggle':
		if target in s:
			s.discard(target)
		else:
			s.add(target)



# 11723 집합 - 비트 집합 사용 S = 0b0
import sys

M = int(sys.stdin.readline())
S = 0b0 # 비트 집합 설정

for i in range(M):
	order = sys.stdin.readline().strip()
	
	try:
		command, num = order.split()
		num = int(num)
		
		if command == 'add':
			S = S | (0b1<<num) # S에 num만큼 왼쪽으로 이동시킨 비트 덮어쓰기
		
		elif command == 'remove':
			S = S & ~(0b1<<num) # S에 num만큼 왼쪽으로 이동시키고 뒤집은 비트 교집합 시키기
		
		elif command == 'check':
			if (S & (0b1<<num)): # 있으면 1
				print(1)
			else:
				print(0)
		
		elif command == 'toggle':
			S = S ^ (0b1<<num)
		
	except:
		if order == 'all':
			S = 0b111111111111111111111
		
		elif order == 'empty':
			S = 0b0

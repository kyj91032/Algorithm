# 스택 자료구조: 한 쪽 끝에서만 자료를 넣고 뺄 수 있는 선형 구조로 되어 있어 선입후출의 구조를 가지는 자료구조이다.

# 스택의 기본 동작 과정

1. 스택 공간을 정의한다.
2. 스택 공간의 끝에서 push와 pop이 이뤄지도록 한다.


# stack 코드

stack = [] # 스택 공간
삽입5 - 삽입2 - 삽입3 - 삽입7 - 삭제 - 삽입1 - 삽입4 - 삭제
stack.append(5) # append()는 리스트의 가장 뒤쪽에 데이터를 삽입한다. (후입)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() # pop()은 리스트의 가장 뒤쪽 데이터를 꺼낸다. (선출)
stack.append(1)
stack.append(4)
stack.pop()
print(stack[::-1]) # 최상단 데이터부터 출력.
print(stack) # 최하단 데이터부터 출력.


# 1874 스택 수열 -> 그냥 짜면, 여러가지 많은 문제들이 저절로 해결되는 문제.. 크면 스택을 채우고, 작으면 조건을 확인해서 pop 하거나, NO 출력

n = int(input())
t = []
for _ in range(n):
	t.append(int(input()))
a = []
for i in range(n):
	a.append(i)
  
s = []
ans = []
flag = 0

i = 1 # i가 밖에 있어서, 반복문 안에서 i가 계속 이어지는데, 이게 상관이 없음.
for k in t:
	while i <= k: # 전 반복에서 i가 이미 현재 k보다 커졌었다면, while문은 실행하지 않음(= 스택이 채워지지 않음)
		s.append(i)
		ans.append("+")
		i += 1
    
	if s[-1] == k:
		s.pop()
		ans.append("-")
	else:
		print("NO")
		flag = 1
		break

if flag == 0:
	for i in ans:
		print(i)



# 1406 에디터 -> 스택의 활용.. 커서를 기준으로 앞뒤 스택을 쪼개기. o(n)커서를 움직이기 -> o(1)제자리에서 append, pop

import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = [] # 처음 시작은 커서 맨 뒤

for _ in range(int(sys.stdin.readline())):
	command = list(sys.stdin.readline().split())
	if command[0] == 'L':
		if st1:
			st2.append(st1.pop()) # 커서 왼쪽 스택에서 팝해서 오른쪽 스택에 추가함으로써 커서를 이동

	elif command[0] == 'D':
		if st2:
			st1.append(st2.pop())

	elif command[0] == 'B':
		if st1:
			st1.pop()

	else:
		st1.append(command[1])

st1.extend(reversed(st2))
print(''.join(st1))


# 10799 쇠막대기 -> 대칭성? 을 스택으로 해결

s = list(input())

now = []
total = 0

for i in range(len(s)):
	if s[i] == '(':
		if s[i+1] == ')':
			total += len(now)
		else:
			now.append('(')
	if s[i] == ')':
		if s[i-1] == '(':
			continue
		else:
			now.pop()
			total += 1

print(total)
'''

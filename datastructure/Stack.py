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
'''

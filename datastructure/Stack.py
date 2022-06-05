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


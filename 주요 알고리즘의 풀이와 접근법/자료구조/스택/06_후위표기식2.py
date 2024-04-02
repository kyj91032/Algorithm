# https://boj-helper.vercel.app/solve/1935?language=python

# 생각 과정
'''
후위 표기식이 스택을 어떤 순서로 활용해서 연산을 하는지 찾아보고 구현했다.
후위 표기식을 돌면서 피연산자는 스택에 넣고, 연산자는 pop하여 스택의 피연산자들과 연산하고 결과를 다시 스택에 넣는다.
마지막 남은 하나가 결과값이 된다.

막힌부분
1. input을 받을 때 rstrip을 해줘야한다.
2. ABC..와 123..을 딕셔너리로 매핑할 때 반복문을 쓸 수도 있지만 큐를 사용할 수도 있다.
'''

# 풀이 코드
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input()) # 첫번째 입력: 피연산자의 개수
s = input() # 두번째 입력: 후위연산식 문자열
dic = {}
stk = []
op = ['/', '-', '*', '+']
num = deque()

for i in range(n):
    num.append(int(input())) # 세번째 입력: 후위 연산식에 차례로 들어갈 숫자들을 큐에 넣어두기

for i in s: # 후위 연산식을 돌면서 A:1 B:2 ... 딕셔너리를 만들기
    if i not in dic and i not in op:
        dic[i] = num.popleft() # 큐에서 빼면서 딕셔너리 값 추가

# 후위표기식을 스택으로 연산하는 로직
for s1 in s:
    if s1 not in op:
        stk.append(dic[s1])
    else:
        x1 = stk.pop()
        x2 = stk.pop()
        if s1 == '+':
            stk.append(x2+x1)
        elif s1 == '-':
            stk.append(x2-x1)
        elif s1 == '/':
            stk.append(x2/x1)
        else:
            stk.append(x2*x1)
    
print(f"{stk[0]:.2f}")



# 피드백 후 정리

'''
문제를 잘 읽기. 알파벳이 26까지만 주어짐. 다시 한바퀴 도는게 아니라
f""을 사용해서 소수점까지 출력하는 방법을 알아두기. f"{변수:.2f}"
'''
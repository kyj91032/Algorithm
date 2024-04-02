# https://boj-helper.vercel.app/solve/1918?language=python

# 생각 과정
'''
어떤 값들을 킵해두고 조건에 따라 꺼내써야한다 ? => 스택 자료구조를 생각할 수 있음
기본적으로 연산자는 stack에 추가한다. 하지만 연산자 우선순위에 따라 바로 이전 연산자 (stack의 top)가 결과에 추가될지 말지를 결정한다.
다음 연산자를 보고 이전 연산자가 결과에 추가될지 말지를 결정하기 위해 스택을 사용하는 것이다.
'''

# 풀이 코드
s = list(input())

stack = [] # 연산자를 저장할 스택
answer = '' # 결과값을 저장할 변수. 문자열 누적 변수로 사용

for ch in s:
    if ch.isalpha(): # 알파벳이면 바로 결과에 추가. 어차피 후위 표기식에서는 문자가 먼저 나오기 때문
        answer += ch
    elif ch == '(': # 여는 괄호는 출력할 일이 없음. 스택에만 추가하고 나중에 조건으로 활용
        stack.append(ch)
    elif ch == '*' or ch == '/': # *, /일 경우엔 이전 연산자가 *, /일 경우에만 이전 연산자를 결과에 추가
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            answer += stack.pop()
        stack.append(ch)
    elif ch == '+' or ch == '-': # +, -일 경우엔 이전 연산자가 여는 괄호가 아닌 모든 경우를 이전 연산자를 결과에 추가
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.append(ch)
    else: # 닫는 괄호일 경우에는 여는 괄호가 나올 때까지 결과에 추가
        while stack and stack[-1] != '(': 
            answer += stack.pop()
        stack.pop() # 여는 괄호를 제거
    
while stack: # 스택에 남아있는 연산자들을 결과에 추가
    answer += stack.pop()
print(answer)


# 피드백 후 정리
'''
1. 스택은 저장하고 특정 조건에 따라 꺼내 쓸때 사용한다. 일단 스택에 값을 저장하고 다른 처리들을 하면서 스택에 저장된 값을 꺼내서 사용한다.
'''
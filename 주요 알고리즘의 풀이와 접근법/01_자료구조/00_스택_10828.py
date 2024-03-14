# https://www.acmicpc.net/problem/10828
# https://boj-helper.vercel.app/solve/10828?language=python

# 생각 과정
'''
1. push 1과 pop, size, empty 등 입력이 주어지는데, 'pop'과 같이 한 단어로 입력이 주어지는 것도 input().split()으로 받아도 되나? 생각을 했다
한 단어도 list(input().split())으로 받아도 된다. ['pop']이런 식으로 리스트로 받아진다.
2. 문제에 나온 대로 if로 분기하며 구현했다.
3. 스택을 리스트로 정의했다.
'''


# 풀이 코드
n = int(input())

stack = []
li = []

for _ in range(n):
    li.append(list(input().split()))

for ca in li:
    if ca[0] == 'push':
        stack.append(ca[1])
    elif ca[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif ca[0] == 'size':
        print(len(stack))
    elif ca[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else: # top
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])


# 피드백 후 정리

'''
a 1
b 2 4
c 
이런 식의 입력이 주어져도, input().split()으로 받아도 된다.

파이썬에서 스택은 리스트로 구현하면 된다.
'''
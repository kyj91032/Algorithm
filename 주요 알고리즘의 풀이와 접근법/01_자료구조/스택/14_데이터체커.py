# https://boj-helper.vercel.app/solve/22942?language=python

# 생각 과정
'''
이 문제를 괄호문제로 생각하기 어려웠다. 양 끝점을 여는 괄호와 닫는 괄호로 생각하면 쉽게 풀 수 있었다.
그렇게 생각하면 다른 문제들과 같이 스택에 어떤 값을 넣고 뺄지를 정해야한다.
이 문제에서는 양 끝점이 같은 쌍인지 확인해야하기 때문에 원의 번호를 같이 넣고 빼야한다.
'''

# 풀이 코드
import sys

def input(): return sys.stdin.readline().rstrip()

n = int(input())
cp = [] # circle point : 원의 양끝점을 저장하는 리스트
for i in range(n):
    x, r = map(int, input().split())
    cp.append((x-r, i)) # 원의 번호를 매겨서 같이 저장
    cp.append((x+r, i))
cp.sort() # 정렬을 해서 x축을 기준으로 정렬되도록 함

stk = []
for c in cp: # 정렬된 양끝 점 순회
    if stk: # 스택에 남아있는 끝점이 있으면
        if stk[-1][1] == c[1]: # 스택의 top의 점이 같은 원의 끝점이면 (원의 번호로 판단)
            stk.pop()
        else: # 다른 원의 끝점이면
            stk.append(c) # 이 경우는 순회하는 동안 stk에서 나가지 못함
    else: # 스택에 아무것도 없으면
        stk.append(c)

if stk:
    print('NO') # 스택에 남아있는 끝점이 있으면 NO
else:
    print('YES')


# 피드백 후 정리
'''
1. 양 끝점을 여는 괄호와 닫는 괄호로 생각하면 쉽게 풀 수 있다.
2. 스택에 어떤 값을 넣고 뺄지를 정해야 한다. 이 문제에서는 원을 식별하기 위한 번호를 좌표와 함께 넣고 뺐다
'''
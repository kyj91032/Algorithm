# https://boj-helper.vercel.app/solve/2800?language=python

# 생각 과정
'''
일단 괄호쌍을 보고 스택이라고 생각했고, 문자열을 돌면서 여는 괄호일때, 닫는 괄호일때를 구현하였다.
닫는 괄호일때 인덱스 쌍이 만들어지므로 이 쌍을 조합을 돌려서 모든 경우를 출력했다.

틀린 부분은, 만약 ((0))이라면 (0,4)를 제거한것과 (1,3)을 제거한 결과가 같아서, 중복된 결과가 나올 수 있다는 것을 몰랐다.
그래서 answer을 set으로 초기화한 후 add를 하다가 마지막에 list로 변환하여 출력해야했다.

테케가 없으면 죽었다 깨어나도 몰랐을거같다..
'''

# 풀이 코드
import sys
from itertools import combinations

def input(): return sys.stdin.readline().rstrip()

s = list(input())
stack = [] # 괄호쌍 -> 일단 스택 만들기
pair = [] # 괄호쌍의 인덱스 쌍
answer = set() # 중복 제거를 위해 set으로 초기화

for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    if s[i] == ')':
        tail = stack.pop()
        pair.append((tail, i)) # 괄호쌍의 인덱스 쌍

for i in range(1, len(pair)+1): # 괄호쌍의 인덱스 쌍을 조합을 돌려서 모든 경우를 출력
    pl = list(combinations(pair, i))
    for pe in pl:
        res = []
        tmp = s[:] 
        for pee in pe:
            first, last = pee[0], pee[1]
            tmp[first] = 'x' # 제거할 부분을 x로 대체
            tmp[last] = 'x'
        for te in tmp:
            if te != 'x':
                res.append(te)
        answer.add(''.join(map(str, res)))

for item in sorted(list(answer)):
	print(item)



# 피드백 후 정리
'''
1. 중복 제거는 set() 자료구조를 사용한다. set에 요소 추가는 add 함수가 있다.
2. 문자열의 요소를 제거할 때 길이가 변하지 않도록 다른 문자로 대체하는 방법을 사용한다.
3. 스택에 어떤 값을 넣고 뺄지를 정해야 한다. 여기서는 인덱스를 넣었다.
4. 반례 확인
'''
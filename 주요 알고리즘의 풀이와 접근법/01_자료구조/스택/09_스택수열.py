# https://boj-helper.vercel.app/solve/1874?language=python

# 생각 과정
'''
처음에 for 문으로 접근하다가 실패해서 답을 봤다.

반복 횟수가 달라지는 반복은 while문으로 구현하는 것이 좋다. -> while문으로 push를 구현한다.
pop은 push를 한 후 스택의 마지막 값이 입력받은 값과 같을 때 실행한다.

'''

# 풀이 코드
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

result = [] # 결과값을 담을 리스트
stk = []

cur = 1 # 현재 가르키는 값. 포인터
# 이 문제의 루프는 반복 횟수가 매번 달라져서 for문으로 구현 어려움
# -> 이렇게 포인터 변수를 두고 이 값을 기준으로 while을 돌리는 것. for문보다 유연하게 loop 구현 가능함
# -> "입력받은 값까지 돌기" 같은 반복 가능.

for _ in range(n):
    seq = int(input()) # 입력받은 값

    # 입력받은 값까지 돌기 (push)
    # 애초에 cur이 seq보다 크다면 실행 안됨. 그래서 연속 pop도 할 수 있는 것
    while cur <= seq:
        stk.append(cur) # push
        result.append('+') # push - '+'
        cur += 1

    # seq 값이 스택의 마지막 값과 같으면 실행 (pop)
    if stk[-1] == seq:
        stk.pop()
        result.append('-')
    else:
        result.clear() # 실패했을 때는 결과값을 비우고 NO 출력
        result.append('NO')
        break

for answer in result:
    print(answer)


# 피드백 후 정리
'''
1. 반복 횟수가 달라지는 반복은 while문으로 구현하는 것이 좋다
2. while문의 조건이 처음부터 만족이 안되면 while문은 실행되지 않음. 
   -> 이것을 이용해 분기와 동시에 반복할 수 있음.
'''

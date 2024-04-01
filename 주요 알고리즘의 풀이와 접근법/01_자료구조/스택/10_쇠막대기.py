# https://boj-helper.vercel.app/solve/10799?language=python

# 생각 과정
'''
괄호의 대칭 문제 -> 스택을 생각했다
스택을 활용한 조금 복잡한 구현
어떤 괄호가 나왔을 때 어떤 처리를 해야하는지 나눠서 구현했다

처음엔 for문을 선택했는데, 레이저를 처리할때 더 유연하게 처리하기 위해 while문을 선택했다.
'''

# 풀이 코드
s = input()

cnt = 0
res = 0

i = 0
while i < len(s):
    if s[i] == '(':
        if s[i+1] == ')': # 레이저인 경우
            res += cnt
            i += 1
        else: # 쇠막대기인 경우
            cnt += 1
    elif s[i] == ')': # 쇠막대기가 끝난 경우
        cnt -= 1
        res += 1
    i += 1

print(res)


# 피드백 후 정리
'''
더 유연한 처리가 필요하면 고민하지 않고 while문을 선택하기
'''
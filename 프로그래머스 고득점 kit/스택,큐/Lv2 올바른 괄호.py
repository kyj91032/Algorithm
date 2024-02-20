# "("문자를 push하고 ")"가 나올떄마다 pop한다는 아이디어만 잡으면 스택으로 푸는 문제라는 걸 알 수 있음

def solution(s):
    cnt = 0
    for i in s:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    if cnt == 0:
        return True
    else:
        return False
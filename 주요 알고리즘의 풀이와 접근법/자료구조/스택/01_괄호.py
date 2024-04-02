# https://boj-helper.vercel.app/solve/9012?language=python

# 생각 과정
'''
괄호의 대칭은 스택과 관련있다는 것을 알고 있어서 cnt 변수를 사용하면 되겠다는 것을 떠올리고 주어진 대로 구현했다.
처음 코드를 완성했을 때는 result가 없이 바로 print를 했는데, NO가 중복해서 출력되는 경우가 있어서 result 변수를 사용했다.
result를 바꿔주고 print는 한번만 하는 식으로 구현했다.
'''

# 풀이 코드
T = int(input())

for i in range(T):
    
    s_input = input()
    cnt = 0
    result = ""
    for c in s_input:
        if cnt < 0:
            result = 'NO'
            break
        if c == '(':
            cnt += 1
        else:
            cnt -= 1
    if cnt == 0:
        result = 'YES'
        print(result)
    else:
        result = 'NO'
        print(result)


# 피드백 후 정리
'''
출력해야 하는 값을 바로 출력하지 않고, 변수에 저장해두고 코드 마지막 부분에서 한번만 출력하는 것이 좋다.
'''
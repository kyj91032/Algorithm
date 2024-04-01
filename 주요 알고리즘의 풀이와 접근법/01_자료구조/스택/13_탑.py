# https://boj-helper.vercel.app/solve/2493?language=python

# 생각 과정
'''
처음에 생각한 방법은 이중 for문을 사용해서 풀어보려고 했지만, 시간복잡도가 O(n^2)이라서 시간초과가 날 것 같아서 다른 방법을 생각함
확인할 필요 없는 탑을 이용해 해결하면 된다고는 생각했다.
근데 이걸 스택을 이용해 풀어내지는 못했다.

스택을 큐처럼 빌때까지 pop을 해주는 방식이라 생소했다.
기본적으로 스택에 탑을 추가하면서, 확인이 필요없는 탑은 스택에서 삭제해주는 방식이다.
현재 탑에서 확인이 필요없는 탑은 이후의 탑에서도 확인이 필요없다는 아이디어가 중요하다. 그렇기 때문에 다음 탑에서도 스택을 이어서 쓸 수 있는 것이다.

'''

# 풀이 코드
n = int(input())
top = list(map(int, input().split()))

stack = []
answer = []

for i in range(n):
    while stack:
        if stack[-1][1] < top[i]:
            stack.pop()
        else:
            answer.append(stack[-1][0] + 1)
            break
    if not stack:
        answer.append(0)
    stack.append([i, top[i]])

print(" ".join(map(str, answer)))


# 피드백 후 정리
'''
1. while queue 뿐만 아니라 while stack도 가능하다. (stack을 순회하는 문제) stack을 이용해 가능한 탑만 순회하는 것
2. 스택에 어떤 값을 넣고 뺄지를 정해야 한다. 
'''
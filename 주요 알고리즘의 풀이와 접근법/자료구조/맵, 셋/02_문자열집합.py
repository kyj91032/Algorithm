# https://boj-helper.vercel.app/solve/14425?language=python

# 생각 과정
'''
in 연산자를 사용해서 풀 수 있는 문제였다.
in 연산자의 경우 List, Set, Dictionary에서 사용할 수 있는데, 이 문제의 경우는 set, dict를 사용하면 시간복잡도가 O(1)이 되어서 효율적으로 풀 수 있었다.
'''

# 풀이 코드 - List에서의 in 연산자
import sys

def input(): return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

s_list = []
answer = 0

for i in range(n):
    s = input()
    s_list.append(s)

for j in range(m):
    s = input()
    if s in s_list:
        answer += 1

print(answer)

# 풀이 코드 - Dic에서의 in 연산자
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
ans = 0
dic = {}
for i in range(N):
    a = input()
    dic[a] = 1
for i in range(M):
    a = input()
    if a in dic:
        ans += 1
print(ans)

# 풀이 코드 - Set에서의 in 연산자
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
ans = 0
s = set()
for i in range(N):
    a = input()
    s.add(a)
for i in range(M):
    a = input()
    if a in s:
        ans += 1
print(ans)


# 피드백 후 정리

'''
1. in 연산자의 자료구조에 따른 시간 복잡도
- list, tuple
    Average: O(n)
    하나하나 순회하기 때문에 데이터의 크기만큼 시간 복잡도를 갖게 됨
- set, dictionary
    Average: O(1), Worst: O(n)
    내부적으로 hash를 통해서 자료들을 저장하기 때문에 시간복잡도가 O(1)가 가능하고 O(n)의 경우에는 해시가 성능이 떨어졌을(충돌이 많은 경우)때 발생
2. 어떤 값이 포함되어있는지를 확인할 때 in 연산자를 사용하고, in 연산자를 사용하는 대상 자료구조를 잘 선택하면(set, dict) 시간복잡도를 줄일 수 있다.
3. dict의 경우 values를 모두 1로 초기화해서 사용할 수 있다. 이때 key값은 중복되지 않아야하므로 set과 비슷한 성격을 가진다.
'''
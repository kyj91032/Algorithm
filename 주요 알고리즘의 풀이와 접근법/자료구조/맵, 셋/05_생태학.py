# https://boj-helper.vercel.app/solve/4358?language=python

# 생각 과정
'''
주어진 n은 1,000,000이고 전체에서 종의 개수를 찾기 위해서는 이중 반복문을 돌아야하지만
이중 반복문을 돌면 시간초과가 날 거라고 생각함.
그래서 종의 이름을 key로하고 개수를 value로 하는 딕셔너리를 만듦. O(n) * O(1) 으로 시간복잡도를 줄인 것.
그리고 정렬은 리스트로 변환해서 정렬함. 딕셔너리는 순서가 없기 때문에.
'''

# 풀이 코드
import sys

def input(): return sys.stdin.readline().rstrip()

tl = []
while True:
    tree = input()
    if not tree:
        break
    tl.append(tree)
    
# tl은 나무 리스트
tn = len(tl) # 나무 총 개수
ts = set(tl) # 나무 집합
tsl = list(ts) # 나무 집합 리스트

td = {} # 나무 딕셔너리 
for t in tsl:
    td[t] = 0

for t in tl: # 나무 리스트에서 나무 딕셔너리에 개수 추가
    if t in td:
        td[t] += 1

for key in td.keys(): # 나무 딕셔너리의 개수를 비율로 바꿈
    td[key] = (td[key] / tn) * 100

result = [(key, value) for key, value in td.items()]
result.sort() # 리스트로 변환 후 정렬

for k, v in result:
    print("%s %.4f" % (k, v))


# 피드백 후 정리
'''
1. 값의 key value 매핑이 보이고, 시간복잡도를 줄여야 할 때 딕셔너리를 사용한다.

2. 딕셔너리를 리스트로 바꿀 때는 dict.keys(), dict.values(), dict.items()를 사용한다.
   items()는 key, value를 튜플로 묶어서 반환하기 때문에 zip을 사용할 필요가 없다.
'''
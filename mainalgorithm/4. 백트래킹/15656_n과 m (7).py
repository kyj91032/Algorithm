# 15657 n과 m (8) - 리스트의 원소 중에 비내림차순 순열

n, m = map(int, input().split())
list = list(map(int, input().split()))

list.sort()

s = []

def rec(start): # bruteforce 인데 반복으로 안되서 재귀로 접근.
    if len(s) == m: # 종료 조건
        print(' '.join(map(str, s)))
        return
    
    for i in list[start:]: # 완전 탐색. 비내림차순이므로 list[start]부터 시작
        # 비내림차순을 위해 중복 제거 조건은 없앤다.
        s.append(i)
        rec(list.index(i)) # 재귀 호출. 비내림차순이므로 list.index(i) + 1이 아닌 list.index(i)로 호출
        s.pop()
rec(0)
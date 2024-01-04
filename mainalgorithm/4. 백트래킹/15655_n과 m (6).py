

# 15655 n과 m (6) - 리스트의 원소 중에 오름차순 순열

n, m = map(int, input().split())
list = list(map(int, input().split()))

list.sort()

s = []

def rec(start): # bruteforce 인데 반복으로 안되서 재귀로 접근.
    if len(s) == m: # 종료 조건
        print(' '.join(map(str, s)))
        return
    
    for i in list[start:]: # 완전 탐색. 오름차순 조건을 고려하여 현재 숫자(list[start]) 보다 높게 가지치기
        if i not in s: # 가지치기 구현. 처음에 111 112 113 121 122 123 131 .. 이렇게 가는 건 단순 bf인데,
                       # 여기서 중복제거 조건을 고려하니 123 124 132 134 142 143 으로 출력해야 하는 거였고, 결국 중복 제거 조건의 삽입이 가지치기를 구현한 것이 되었다.
            s.append(i)
            rec(list.index(i) + 1) # 재귀 호출
            s.pop()
rec(0)
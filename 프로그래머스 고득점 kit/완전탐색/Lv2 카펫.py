def solution(brown, yellow):
    
    li = [1,2,3] # yellow가 1,2,3일땐 모양이 결정되므로 따로 처리
    if yellow in li:
        v = yellow
        h = 1
        return [v+2, h+2]
    
    for h in range(2, yellow//2 + 1):
        if yellow % h == 0:
            v = yellow // h
            tmpB = v * 2 + h * 2 + 4
            if tmpB == brown:
                return [v+2, h+2]

# 완전탐색을 하되, 결정할 수 있는 것을 먼저 결정하면서 탐색하기
# 이 문제에서는 yellow를 기준으로 가능한 경우를 탐색하면서 그에 맞는 brown을 계산하면 가로, 세로를 찾을 수 있다.
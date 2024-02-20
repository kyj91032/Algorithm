# 직사각형을 긴 변을 가로로, 작은변을 세로로 정리해버리는 아이디어가 중요
# 원래 완전 탐색하면서 바꿔주는 방법을 생각했는데, 이 과정에서 대칭성을 떠올렸을때 이 때 대칭성 때문에 가로 세로를 정리해도 상관없다는 걸 알았어야함

def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])

    return max(w) * max(h)
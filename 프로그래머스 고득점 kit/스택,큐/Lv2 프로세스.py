# 문제에 큐가 명시되어 있음 -> 큐 써서 풀면 됨

def solution(priorities, location):
    
    que = [(a, b) for a, b in zip(range(len(priorities)), priorities)]
    # emumerate를 쓰면 더 간단하게 가능
    # que = [(a, b) for a, b in enumerate(priorities)] index와 엮어줌

    result = []
    while len(que) > 0:
        a = que.pop(0)
        if len(que) == 0:
            result.append(a)
        else:
            if a[1] < max(que, key = lambda x : x[1])[1]:
                que.append(a)
            else:
                result.append(a)
    
    for i in result:
        if i[0] == location:
            return result.index(i) + 1


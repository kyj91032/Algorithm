# dungeons가 8이하인 순간부터 완전탐색일 확률 높음 -> 실제로 O(n!)

from itertools import permutations

def solution(k, dungeons):

    answer = -1

    n = len(dungeons)
    order = [i for i in range(n)]

    for ord in list(permutations(order)):
        tmp = 0
        ktmp = k
        for o in ord:
            if ktmp >= dungeons[o][0]:
                if ktmp - dungeons[o][1] >= 0:
                    tmp += 1
                    ktmp -= dungeons[o][1]
                    max(tmp, answer)
                else:
                    max(tmp, answer)
                    continue
            else:
                max(tmp, answer)
                continue
        
    return answer

solution(80 ,[[80,20],[50,40],[30,10]])
'''
1. 트리가 그려짐 -> 재귀 판단
2. 종료조건, 재귀조건, 상태전이 구현
'''

def solution(numbers, target):
    answer = rec(numbers, target, 0)
    return answer

def rec(numbers, target, depth): # depth가 상태, numbers, target은 초기값
    '''
    depth를 len(numbers)로 하지 않는게 좋음. 종료조건에서 그냥 재귀 자체의 깊이로 중단하는 게 안정적
    '''
    answer = 0
    if depth == len(numbers): # 종료 조건
        print(numbers)
        if sum(numbers) == target:
            return 1 # 이게 answer += 1, answer -= 1로 연결됨
        else: return 0
    else:
        answer += rec(numbers, target, depth+1)
        numbers[depth] *= -1 # 부호 바꿔서 재귀
        answer += rec(numbers, target, depth+1)
        return answer
# set과 dict는 해시테이블로 구현되어있어서 O(1)의 시간복잡도를 가진다.

# 종류가 같다, 식별 -> set, dict과 같은 자료구조 사용할 확률이 높다.

def solution(nums):
    
    answer = 0
    
    length = len(set(nums)) # set을 이용해서 중복을 제거하고 길이를 구한다.
    r = len(nums) // 2
    
    if length >= r:
        answer = r
    else:
        answer = length
    
    return answer

# 다른 사람의 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls))) # 조건 분기가 필요없음. min 함수를 이용해서 더 작은 값을 return 하면 됨.

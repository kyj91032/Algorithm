from collections import Counter

# 종류가 매핑 -> 딕셔너리 사용

def solution(clothes):

    answer = 1

    cloth_map = {}
    for i in range(len(clothes)): # O(N)
        cloth_map[clothes[i][0]] = clothes[i][1] 
    
    category_count = Counter(cloth_map.values()) # O(종류 개수)
    # Counter는 iterable한 객체를 받아서 각 요소의 개수를 세어서 dict로 만들어준다

    for i in category_count.values():
        answer = answer * (i + 1)

    return answer - 1


### Counter를 쓰지 않고 개수를 바로 딕셔너리로 받은 풀이
def solution(clothes):
    answer = 1

    cloth_map = {}

    # 옷의 종류별 개수를 수동으로 세기
    for cloth in clothes:
        cloth_type = cloth[1]
        if cloth_type in cloth_map:
            cloth_map[cloth_type] += 1
        else:
            cloth_map[cloth_type] = 1

    # 각 종류별로 개수를 곱하여 모든 조합 구하기
    for count in cloth_map.values():
        answer *= (count + 1)

    return answer - 1
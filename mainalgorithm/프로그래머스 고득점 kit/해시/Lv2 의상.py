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

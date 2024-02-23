'''
반복 vs 재귀
바텀업 vs 탑다운
itertools vs recursion
'''

# itertools를 사용한 바텀업 풀이
from itertools import product

def solution(word):
    words = [] # 사전
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            # product는 중복순열을 만들어준다. repeat에 숫자를 넣어주면 그만큼의 길이의 중복순열을 만들어준다.
            # 반복문까지 써서 1~5까지의 길이의 중복순열을 만들어준다.
            words.append(''.join(list(c)))

    words.sort()
    return words.index(word) + 1


# 재귀
# 재귀함수로 단어 사전 list를 만들고 인덱스를 반환하는 방법
def solution(word):
    answer = 0
    word_list = [] # 단어사전 -> 전역변수
    words = 'AEIOU'
    
    def dfs(w):
        if len(w) == 5: 
            return
        for i in range(len(words)): # 순회하면서 
            word_list.append(w + words[i]) # 단어사전에 추가
            dfs(w + words[i]) # 추가한 후 그 상태(현재 문자열 필요)에서 다시 로직 수행. 상태 전이
            # 문쟈열 길이를 넣어주는 경우가 있는데, 현재는 그냥 문자열 받고 길이 구하면되니까 필요없다.
            '''
            그래도 depth를 두고 하는게 좋음 -> Lv2 타겟넘버 참고
            '''
            
    dfs("")
    
    return word_list.index(word)+1

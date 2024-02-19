# 중복순열 product vs 백트래킹 dfs

from itertools import product

def solution(word):
    words = [] # 사전
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            # product는 중복순열을 만들어준다. repeat에 숫자를 넣어주면 그만큼의 길이의 중복순열을 만들어준다.
            # 1~5까지의 길이의 중복순열을 만들어준다.
            words.append(''.join(list(c)))

    words.sort()
    return words.index(word) + 1


# dfs로 풀기
vowels = ['A', 'E', 'I', 'O', 'U']
answer = 0 
idx = -1 # 몇 번째인지
def solution(word):
    def dfs(cnt, s): # cnt: 길이, s: 문자열
        global answer, idx
        if cnt <= 5:
            idx += 1
            if s == word:   
                answer = idx
        else:
            return
        for i in range (5):
            dfs(cnt + 1, s + vowels[i])
    dfs(0, '')
    return answer
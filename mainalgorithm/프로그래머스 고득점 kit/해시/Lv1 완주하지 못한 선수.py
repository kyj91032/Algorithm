# participants와 completion의 길이는 1 이상 100,000 이하 -> O(NlogN) 이하의 알고리즘 설계 필요

# 비교하는 문제 -> 정렬 혹은 Hash를 이용할 확률이 높다

# Sort 를 이용한 풀이
def solution(participant, completion):
    answer = ''

    # 1. 두 list를 sorting한다
    participant.sort() # O(NlogN)
    completion.sort() # O(NlogN)

    # 2. completeion list의 len만큼 participant를 찾아서 없는 사람을 찾는다
    for i in range(len(completion)): # O(N)
        if(participant[i] != completion[i]): # O(1)
            return participant[i]

    # 3. 전부 다 돌아도 없을 경우에는 마지막 주자가 완주하지 못한 선수이다.
    return participant[len(participant)-1]


# Hash를 이용한 풀이
def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    
    # 1. Hash : Participant의 dictionary 만들기
    # 2. Participant의 sum(hash) 구하기
    for part in participant:
        hashDict[hash(part)] = part # key: hash, value: part 로 dictionary 만들기
        sumHash += hash(part) # hash 값의 합 구하기 -> 완주하지 못한 선수의 hash 값은 이 값에서 빼면 된다
    
    # 3. completion의 sum(hash) 빼기
    for comp in completion:
        sumHash -= hash(comp)
    
    # 4. 남은 값이 완주하지 못한 선수의 hash 값이 된다
    return hashDict[sumHash]

# Counter 를 이용한 풀이
import collections
def solution(participant, completion):

    answer = collections.Counter(participant) - collections.Counter(completion)
    
    return list(answer.keys())[0]

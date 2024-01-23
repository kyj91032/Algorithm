# 같은 것을 탐색할 시 O(N^2)의 시간복잡도라면 hash를 이용하면 O(N)으로 줄일 수 있다.

# hosh를 이용한 풀이
def solution(phone_book):
    hash_map = {} # dictionary를 hash_map으로 사용 -> 검색 시 O(1)의 시간복잡도를 가짐
    for phone_number in phone_book:
        hash_map[phone_number] = 1 # List를 hash_map으로 만드는 방법
    for phone_number in phone_book:
        temp = ""
        for number in phone_number: # 여기까지 O(N). phone_number의 길이는 < 20이므로 이중반복문 O(N^2)이 아님 20 * O(N) = O(N)
            temp += number
            if temp in hash_map and temp != phone_number: # hashmap에 자기 자신을 제외한 key가 존재하면 False. dict이므로 O(1)
                return False
    return True 

# 정렬을 이용한 풀이
def solution(phone_book):    
    p = sorted(phone_book)

    for i in range(len(p)-1):
        first = p[i]
        second = p[i+1]
        flen = len(first)
        if len(second) > len(first) and first == second[0:flen]:
            return False
    
    return True

# 다른 사람의 풀이
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]): # 두개 이상의 list를 동시에 순회할 때 zip을 사용할 수 있음
        if p2.startswith(p1): # startswith을 사용하면 문자열의 시작부분이 일치하는지 확인할 수 있음
            return False
    return True


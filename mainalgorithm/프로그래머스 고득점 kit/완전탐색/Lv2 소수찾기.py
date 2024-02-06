import math
from itertools import permutations

def solution(numbers):

    max = 10000000 # 에라토스테네스의 체를 이용해 소수 테이블 미리 생성
    array = [True for _ in range(max + 1)]
    for i in range(2, int(math.sqrt(max)) + 1):
        if array[i] == True:
            j = 2
            while j * i <= max:
                array[i * j] = False
                j += 1
    array[1] = False
    array[0] = False
    
    numlist = list(numbers)

    permlist = []
    for r in range(1, len(numlist) + 1):
        for perm in permutations(numlist, r):
            permlist.append(int(''.join(perm))) # perm은 ('1','7') -> ''.join(perm)하면 '17' -> int하면 17
    # permutation을 쓸 수 있는 근거는 n, r의 최대값이 7이기 때문에 O(n) * O(n!) 충분히 가능

    answer = 0
    permlist = list(set(permlist))
    # permlist에 중복 제거. 만약 0,1,1이 numlist라면 permutations는 '1' 두개를 다른 것 취급함. 그래서 011, 011이렇게 중복이 발생
    for p in permlist:
        if array[p] == True:
            answer += 1
    
    return answer

solution("011")
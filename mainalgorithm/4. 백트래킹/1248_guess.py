# 1248 guess (부호 행렬)

def ck(idx): # 합의 부호가 맞는지 확인
    hap = 0
    for i in range(idx, -1, -1):
        hap += result[i] # result에 integer sequence 저장, hap으로 현재 idx 까지의 합 정의
        if hap == 0 and S[i][idx] != 0:
            return False
        elif hap < 0 and S[i][idx] >= 0:
            return False
        elif hap > 0 and S[i][idx] <= 0:
            return False
    return True

def solve(idx):
    if idx == N: # 깊이에 따른 종료조건
        return True
    if S[idx][idx] == 0: # i = j 일때 S 가 0 이면 그 때 Ai가 0 이라는 것
        result[idx] = 0
        return solve(idx + 1) # 재귀 호출
    for i in range(1, 11): # 1부터 10까지 bf
        result[idx] = S[idx][idx] * i # i = j 일때 S의 값이 그 때 Ai의 부호 의미.
        if ck(idx) and solve(idx + 1): # 부호 합이 맞고, 재귀 호출이 성공했다면, i 다음 숫자. 실패하면 종료 호출
            return True
    return False

N = int(input())
arr = list(input())
S = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(i, N):
        temp = arr.pop(0)
        if temp == '+':
            S[i][j] = 1
        elif temp == '-':
            S[i][j] = -1

result = [0] * N
solve(0)
print(' '.join(map(str, result)))


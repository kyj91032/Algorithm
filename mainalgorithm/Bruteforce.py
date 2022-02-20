# 브루트포스 알고리즘: 완전 탐색

# 완전 탐색의 기본 동작 과정
'''
1. 처음부터 끝까지 모두 확인한다
'''

''' python

h = int(input()) # 시간 완전탐색. 86400개의 경우의 수. 3중 반복문 이용
cnt = 0
for i in range(n + 1):
	for j in range(60):
		for k in range(60):
			if '3' in str(i) + str(j) + str(k):
				cnt += 1
print(cnt)

'''

''' python; 3085 사탕게임

import sys
input = sys.stdin.readline

def check(arr): # '연속되는 숫자의 최댓값 확인하는 코드' 따로 떼서 함수로 만들기. 이렇게 쪼개서 생각할 수 있어야 함. 사실상 2차원 선형탐색.
    n = len(arr)
    max = 1

    for i in range(n):
        cnt = 1
        for j in range(1, n): # 가로 전체 탐색
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > max: # 매번 최댓값 갱신
                max = cnt
        cnt = 1
        for j in range(1, n): # 세로 전체 탐색
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > max:
                max = cnt
    return max


n = int(input())
arr = [list(input()) for _ in range(n)] # 이중 리스트로 바로 입력받기
answer = 0

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            
            temp = check(arr)

            if temp > answer:
                answer = temp
               
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        if i + 1 < n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            
            temp = check(arr)

            if temp > answer:
                answer = temp
            
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            
print(answer)

'''

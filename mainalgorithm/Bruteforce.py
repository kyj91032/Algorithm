# 브루트포스 알고리즘: 완전 탐색

# 완전 탐색의 기본 동작 과정
'''
1. 처음부터 끝까지 모두 확인한다. (1 ~ 3차원 선형탐색, 최대 최소 선형탐색, 
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

def check(arr): # '연속되는 숫자의 최댓값 확인하는 코드' 따로 떼서 함수로 만들기. 이렇게 쪼개서 생각할 수 있어야 함. 그리고 사실상 완전탐색 형태는 2차원 선형탐색.
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

''' python; 1476 날짜 계산

a, b, c = map(int, input().split())
y = 1 # 연도 자체(답)를 1부터 선형 탐색함. 답이 y라고 하면 맞나?를 계속 확인

while True:
    if (y - a) % 15 == 0 and (y - b) % 28 == 0 and (y - c) % 19 == 0:
        print(y)
        break
    y += 1

'''

''' python; 1107 리모컨

import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
broken = list(map(int, input().split()))

min_count = abs(100 - target) # 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우. 최댓값을 초기값으로 설정.

for nums in range(1000001): # 고장난 채널을 제외한 모든 채널 탐색
    nums = str(nums)
    
    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums)) # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트

print(min_count)

'''


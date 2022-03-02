# 브루트포스 알고리즘: 완전 탐색

# 완전 탐색의 기본 동작 과정
'''
1. 처음부터 끝까지 모두 확인(탐색)한다. (1 ~ 3차원 선형탐색, 최대최소 선형탐색, 좌표 이동경로 정의 후 탐색 or 시뮬레이션, DFS, BFS)
2. 불필요한 탐색을 줄일 가능성이 있는지 알아본다. (1 ~ 3차원 선형탐색의 범위축소 ex) += 1 대신 += k, 백트래킹)
'''

''' 시간 완전탐색

h = int(input()) # 86400개의 경우의 수. 3중 반복문 이용
cnt = 0
for i in range(n + 1):
	for j in range(60):
		for k in range(60):
			if '3' in str(i) + str(j) + str(k):
				cnt += 1
print(cnt)
'''


''' 3085 사탕게임

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


''' 1476 날짜 계산

a, b, c = map(int, input().split())
y = 1 # 연도 자체(답)를 1부터 선형 탐색함. 답이 y라고 하면 맞나?를 계속 확인

while True:
    if (y - a) % 15 == 0 and (y - b) % 28 == 0 and (y - c) % 19 == 0:
        print(y)
        break
    y += 1
'''


''' 6064 카잉달력

T = int(input())

for _ in range(T):
	M, N, x, y = map(int, input().split())
	year = x
	while 1:
		if year % N == y % N: # 연도 year를 1부터 탐색할 필요 없이, year += M으로 탐색해도 된다.
			print(year)
			break
		year += M
		if year > M * N:
			print(-1)
			break
'''


''' 1107 리모컨

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


''' 나이트 움직이기

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 문자을 숫자로 대응. 아스키코드 이용

steps = [(-2, -1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] # 나이트 이동 경로 8가지 정의

cnt = 0
for step in steps:
    next_row = row + step[0] # 열 이동
    next_column = column + step[1] # 행 이동
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8:
        cnt += 1
print(cnt)
'''


''' 유닛의 자동 이동

n, m = map(int, input().split())

x, y, direction = map(int, input().split())

d = [[0] * m for _ in range(n)]
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0] # 북, 동, 남, 서 방향 정의
dy = [0, 1, 0, -1]

def turn_left(): # 왼쪽으로 회전 함수
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue #
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
'''


''' 14500 테트로미노

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

s = []
tetromino = [[[0, 1], [0, 2], [0, 3]], [[1, 0], [2, 0], [3, 0]], # 테트로미노를 이동 경로라고 생각했을 때 좌표 이동 경로 정의
[[0, 1], [1, 0], [1, 1]], [[1, 0], [2, 0], [2, 1]],
[[1, 0], [2, 0], [2, -1]], [[0, 1], [0, 2], [1, 0]],
[[0, 1], [0, 2], [1, 2]], [[0, 1], [1, 1], [2, 1]],
[[0, 1], [1, 0], [2, 0]], [[0, 1], [0, 2], [-1, 2]],
[[1, 0], [1, 1], [1, 2]], [[1, 0], [1, 1], [2, 1]],
[[1, 0], [1, -1], [2, -1]], [[0, 1], [-1, 1], [-1, 2]],
[[0, 1], [1, 1], [1, 2]], [[0, 1], [0, 2], [1, 1]],
[[1, 0], [1, 1], [2, 0]], [[1, 0], [1, -1], [2, 0]],
[[0, 1], [0, 2], [-1, 1]]

for i in range(n):
    s.append(list(map(int, input().split())))
result = 0
for i in range(n): # 좌표 완전 탐색 하면서 이동 경로 탐색
    for j in range(m):
        for k in tetromino:
            try:
                sum_n = s[i][j] + s[i + k[0][0]][j + k[0][1]] + s[i + k[1][0]][j + k[1][1]] + s[i + k[2][0]][j + k[2][1]]
            except:
                sum_n = 0
            result = max(result, sum_n)
print(result)
'''


''' 15649 N과 M(1)

n, m = list(map(int, input().split()))
 
s = []
 
def dfs(): # 백트래킹 함수
    if len(s) == m: # 종료조건
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs() # 백트래킹 가지치기, 왔던 길로 돌아가 다시 탐색.
            s.pop()
 
dfs()
'''

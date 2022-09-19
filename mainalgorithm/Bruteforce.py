# 브루트포스 알고리즘: 완전 탐색

# 완전 탐색의 기본 동작 과정

1. 처음부터 끝까지 모두 확인(탐색)한다. for (반복과 1 ~ 3차원 선형탐색, 재귀와 깊이 조건, 최대최소 선형탐색, 좌표 이동경로 정의 후 탐색 or 시뮬레이션, 함수형 프로그래밍, 비트마스크)
2. 주어진 조건을 제외하고, 불필요한 탐색을 줄일 가능성이 있는지 알아본다. if (탐색의 범위축소 ex) += 1 대신 += k, 백트래킹)
3. 분류해서 부분 문제를 해결한다. def
+ 예시(최소한 처음중간끝이 나뉘도록)를 가지고 먼저 구현한 뒤 일반화 해나가기


# 시간 완전탐색

h = int(input()) # 86400개의 경우의 수. 3중 반복문 이용
cnt = 0
for i in range(n + 1):
	for j in range(60):
		for k in range(60):
			if '3' in str(i) + str(j) + str(k):
				cnt += 1
print(cnt)



# 3085 사탕게임

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



# 1476 날짜 계산

a, b, c = map(int, input().split())
y = 1 # 연도 자체(답)를 1부터 선형 탐색함. 답이 y라고 하면 맞나?를 계속 확인

while True:
    if (y - a) % 15 == 0 and (y - b) % 28 == 0 and (y - c) % 19 == 0:
        print(y)
        break
    y += 1



# 6064 카잉달력

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



# 1107 리모컨

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



# 나이트 움직이기

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



# 유닛의 자동 이동

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



# 14500 테트로미노

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



# n과 m (3) 완전 탐색의 재귀적 구현 recursive bruteforce

n, m = list(map(int, input().split()))
 
s = []

def rec(): # bruteforce 인데 반복으로 안되서 재귀로 접근.
    if len(s) == m: # 종료 조건
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1): # 완전 탐색
            s.append(i)
            rec() # 재귀 호출
            s.pop()
rec()



# 9095 1,2,3 더하기 - 완전 탐색의 재귀적 구현

n = int(input())

def sums(n):
    if n == 1:
        return(1)
    elif n == 2:
        return(2)
    elif n == 3:
        return(4)
    else:
        return sums(n-1) + sums(n-2) + sums(n-3)
        
for i in range(n):
    a = int(input())
    print(sums(a))



# 14501 퇴사

import sys
input = sys.stdin.readline

n = int(input())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))

M = 0

def go(day, total):
    global M
    if day == n:  # n에 알맞게 도착했을 때, 정답이 될 수 있다. # 깊이에 따른 종료조건.
        M = max(M, total)
        return
    if day > n:  # n을 초과한다면 범위 안에 일을 못끝내므로, 정답이 될 수 없다. # 깊이에 따른 종료조건
        return
    go(day + 1, total) # 이번 day는 일을 하지 않고 그냥 넘어간다!
    go(day + s[day][0], total + s[day][1]) # 이번 day일을 처리한다, 기간도 점프한다! # 모든 경우 재귀 호출해서 M값 최신화하기 (최대최소 bf + 재귀적 구현)

go(0, 0) # day는 0, total도 0부터 시작.
print(ans)



# 10819 차이를 최대로 - 최대최소 bf

import sys
input = sys.stdin.readline

def np(pl): # next permutation 알고리즘 (재귀로 구현하는 순열보다 빠름.)
	x = 0
	for i in range(len(pl) - 1, 0, -1):
		if pl[i - 1] < pl[i]:
			x = i - 1
			break
	for i in range(n - 1, 0, -1):
		if pl[x] < pl[i]:
			pl[x], pl[i] = pl[i], pl[x]
			pl = pl[:x + 1] + sorted(pl[x + 1:])
			return pl
	return [-1]


n = int(input())
a = list(map(int, input().split()))

a.sort()

ans = 0 # 최대값 저장, 최신화

s = 0
for j in range(len(a) - 1):
    s += abs(a[j] - a[j+1])
if s > ans:
    ans = s

arr = a

while 1:
	arr = np(arr)
	if arr == [-1]:
		break
	s = 0
	
	for j in range(len(arr) - 1):
		s += abs(arr[j] - arr[j+1])
	if s > ans:
		ans = s
print(ans)



# 14319 종이조각 - 비트마스킹

import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

paper = []
for _ in range(n):
	paper.append(list(map(int, input().rstrip())))

ans = []

for i range(1 << n*m): # 2의 n * m승 가지의 경우의 수 모두 확인
	total = 0
	for row in range(n):
		rowsum = 0
		for col in range(m):
			idx = row * m + col # idx는 주어진 배열의 번호
			if i & (1 << idx) != 0: # 대충 알겠는데, 1. 이렇게 확인하면 모든 경우의 수가 확인되는가? 2. 이 풀이를 떠올릴만한 개연성이 있나?
				rowsum = rowsum * 10 + paper[row][col]
			else:
				total += rowsum
				rowsum = 0
		total += rowsum
	
	for col in range(m):
		colsum = 0
		for row in range(n):
			idx = row * m + col
			if i & (1 << idx) == 0:
				colsum = colsum * 10 + paper[row][col]
			else:
				total += colsum
				colsum = 0
		total += colsum
	ans.append(total)

print(max(ans))


# 16035 배열 돌리기3 - arr을 바로 바꾸기보단 함수 쓰고 tmp에 담아서 arr에 넣어 바꾸기

import sys
input=sys.stdin.readline

def cal1(arr):
    temp=[[0]*m for _ in range(n)]
    for i in range(n):
        temp[i]=arr[n-i-1]
    return temp
def cal2(arr):
    temp=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j]=arr[i][m-j-1]
    return temp
def cal3(arr,n,m):
    temp=[[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j]=arr[n-j-1][i]
    return temp
def cal4(arr,n,m):
    temp=[[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j]=arr[j][m-i-1]
    return temp
def cal5(arr):
    temp=[[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            temp[i][j+m//2]=arr[i][j]
    for i in range(n//2):
        for j in range(m//2,m):
            temp[i+n//2][j]=arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2,m):
            temp[i][j-m//2]=arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2):
            temp[i-n//2][j]=arr[i][j]
    return temp
def cal6(arr):
    temp=[[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            temp[i+n//2][j]=arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2):
            temp[i][j+m//2]=arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2,m):
            temp[i-n//2][j]=arr[i][j]
    for i in range(n//2):
        for j in range(m//2,m):
            temp[i][j-m//2]=arr[i][j]
    return temp

n,m,r=map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(n)]
cals=list(map(int, input().split()))

for cal in cals:
    if cal==1:
        arr=cal1(arr)
    elif cal==2:
        arr=cal2(arr)
    elif cal==3:
        arr=cal3(arr,n,m)
        n,m=m,n
    elif cal==4:
        arr=cal4(arr,n,m)
        n,m=m,n
    elif cal==5:
        arr=cal5(arr)
    else:
        arr=cal6(arr)

for i in arr:
    print(*i)

	     
# 16926 배열돌리기3 - 복잡한 bf는 예시를 이용해 일반화를 시작하기

import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m) // 2):
    	# x, y 는 돌려지는 배열중 가장 첫번째 배열 인덱스
        x, y = i, i
        temp = data[x][y]
                            # 안쪽까지 계속 고려해야하기 때문에 n-i랑 m-i까지로 범위설정
        for j in range(i + 1, n - i):  #좌
            x = j
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

        for j in range(i + 1, m - i):  #하
            y = j
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

        for j in range(i + 1, n - i):  #우
            x = n - j - 1
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

        for j in range(i + 1, m - i):  #상
            y = m - j -1
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

for i in range(n):
    for j in range(m):
        print(data[i][j], end=' ')
    print()


# 16927 배열돌리기2 - 제자리에 오는 걸 고려해서 r을 나눌생각, 더 나아가서 고리마다 다른 제자리 값을 적용해주는 것.

import math

N, M, R = map(int, input().split())

NUMBERS = [list(map(int, input().split())) for _ in range(N)]

turns = []
for k in range(min(N, M)//2):
    turns.append(2*((N-(2*k))+(M-(2*k)))-4)


for k in range(min(N,M)//2):
    for r in range(R%turns[k]):
        temp = NUMBERS[k][k]
        for i in range(1+k, M-k):
            NUMBERS[k][i-1] = NUMBERS[k][i]

        for i in range(1+k, N-k):
            NUMBERS[i-1][M-1-k] = NUMBERS[i][M-1-k]

        for i in range(1+k, M-k):
            NUMBERS[N-1-k][M-i]=NUMBERS[N-1-k][M-1-i]

        for i in range(1+k, N-k):
            NUMBERS[N-i][k] = NUMBERS[N-1-i][k]

        NUMBERS[1+k][k] = temp

for n in NUMBERS:
    print(" ".join(map(str,n)))


# 14499 주사위 굴리기 - 어떻게 주사위가 구르는 것을 구현하지?? -> 

인덱스 0부터 5까지 각각의 인덱스가 위쪽, 뒤쪽, 오른쪽, 왼쪽, 앞쪽, 바닥 이라고 했을 때
[1, 2, 3, 4, 5, 6] => [3, 2, 6, 1, 5, 4] 로 변했음을 알 수 있다
마찬가지로 다른 방향으로 굴렸을 때에 대해서도 어떻게 변했는지를 알면 이 문제를 다 풀었다고 볼 수 있다.
이러한 규칙을 turn함수에 정의를 해놓고
굴려야 하는 타이밍에 함수를 실행시키면 된다.

n, m, x, y, k = map(int, input().split())

board = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0] # 전개도를 인덱싱해서 주사위 굴리기를 구현함

def turn(dir): # 동서남북 전개도 리스트가 바뀌는 걸 함수로 구현
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

for i in range(n):
    board.append(list(map(int, input().split())))

comm = list(map(int, input().split()))

nx, ny = x, y
for i in comm:
    nx += dx[i-1]
    ny += dy[i-1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m: # 나가면 다음 반복으로
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    turn(i)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0

    print(dice[0])



# 14890 경사로 - 불필요한 탐색을 줄일 때, 큰 것 먼저 걸러내기. 여기선 차이가 1 넘는걸 먼저 거르고, 현재>이전 이전>현재로 나눠서 경사로가 가능한지 탐색

import sys

def pos(now):
    """
    1. 차이가 1만 경사로 설치 가능
    2. 현재 높이 < 이전 높이, 경사로 설치를 위해 오른쪽 스캔 (낮은 곳에 경사로 설치)
    3. 현재 높이 > 이전 높이, 경사로 설치를 위해 왼쪽 스캔 (낮은 곳에 경사로 설치)
    :param i:
    :return:
    """
    for j in range(1, n):
        if abs(now[j] - now[j - 1]) > 1:   # 1. 차이가 1만 가능
            return False
        if now[j] < now[j - 1]:            # 2.  현재 < 이전, 경사로를 만들기 위해 오른쪽을 스캔함(낮은 곳에 경사로 설치)
            for k in range(l):  # l 만큼 경사로 너비 필요 
                if j + k >= n or used[j + k] or now[j] != now[j + k]: # 범위 넘어감 or 이미 설치함 or 낮은 곳의 높이가 다른 경우, 그만  
                    return False
                if now[j] == now[j + k]:   # 높이가 같은 경우 사용 여부 체크 
                    used[j + k] = True
        elif now[j] > now[j - 1]:         # 3.  현재 > 이전, 경사로를 만들기 위해 왼쪽을 스캔함
            for k in range(l):
                if j - k - 1 < 0 or now[j - 1] != now[j - k - 1] or used[j - k - 1]:  # 범위 넘어감 or 이미 설치함 or 낮은 곳의 높이가 다른 경우, 그만
                    return False
                if now[j - 1] == now[j - k - 1]:   # 높이가 같은 경우 사용 여부 체크 
                     used[j - k - 1] = True
    return True   # 모두 문제없이 설치된 경우 가능함을 출력 

n, l = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = 0

# 1. 가로 확인
for i in range(n):
    used = [False for _ in range(n)]  # 사용 여부
    if pos(graph[i]):  # 현재 확인할 길을 넣어준다.
        result += 1

# 2. 세로 확인
for i in range(n):
    used = [False for _ in range(n)]
    if pos([graph[j][i] for j in range(n)]):  # 현재 확인할 길을 넣어준다.
        result += 1

print(result)



# 15662 톱니바퀴2 - 문제를 쪼개서 해결할 줄 알아야함.. 돌리는 함수따로 쓰기, 돌 수 없는 톱니바퀴 분류 먼저 하기

# 움직이지 못하는 톱니바퀴 저장
# [1-2] = True, [2-3] = True 와 같은 방식으로 저장
def dont_move():
    dont_move = [False] * (T - 1)
    # 비교
    for i in range(T - 1):
        if wheel[i][2] == wheel[i + 1][6]:
            dont_move[i] = True
    return dont_move


# 톱니바퀴 회전
def move(wheel, dir):
    if dir == 1:
        wheel[0], wheel[1], wheel[2], wheel[3], \
        wheel[4], wheel[5], wheel[6], wheel[7] = wheel[7], wheel[0], wheel[1], wheel[2], \
                                                 wheel[3], wheel[4], wheel[5], wheel[6]
    else:
        wheel[0], wheel[1], wheel[2], wheel[3], \
        wheel[4], wheel[5], wheel[6], wheel[7] = wheel[1], wheel[2], wheel[3], wheel[4], \
                                                 wheel[5], wheel[6], wheel[7], wheel[0]


T = int(input())
wheel = []  # 톱니바퀴 정보저장
for _ in range(T):
    wheel.append(list(map(int, input())))
N = int(input())

for _ in range(N):
    t, dir = map(int, input().split())  # 톱니바퀴 0 ~ T - 1 번까지로 계산
    fixed = dont_move()  # 움직이지 못하는 톱니바퀴 정보 저장
    # fixed에는 [True,False,True]..와 같은 형식으로 저장된다.
    # fixed[0] = True -> [0-1번 관계에서는 톱니바퀴가 돌지않음]
    # fixed[1] = False -> [1-2번 관계에서는 톱니바퀴가 돌 수 있음]

    move(wheel[t - 1], dir)  # 우선 입력받은 t-1 번의 톱니바퀴는 무조건 회전
    temp_dir = -dir  # 방향반대로저장
    plus = t - 1  # 입력받은 톱니바퀴의 오른쪽 톱니바퀴들을 확인한다.
    while plus <= T - 2:  # 톱니바퀴의 관계가 T-2개 까지 있기때문에
        if not fixed[plus]:  # 만약 해당 톱니바퀴가 돌 수 있다면
            move(wheel[plus + 1], temp_dir)  # 톱니바퀴를 해당방향으로 돌린다.
        else:  # 돌 수 없다면
            break  # 탈출
        temp_dir = -temp_dir  # 해당방향과 반대로 돈다.
        plus += 1  # 톱니바퀴 한개 증가

    minus = t - 1 - 1  # 입력받은 톱니바퀴의 왼쪽 톱니바퀴들을 확인한다.
    temp_dir = -dir  # 방향 반대로 저장
    while minus >= 0:  # 톱니바퀴의 관계가 0부터 있으므로
        if not fixed[minus]:  # 만약 해당 톱니바퀴가 돌 수 있다면
            move(wheel[minus], temp_dir)  # 톱니바퀴를 해당방향으로 돌린다.
        else:  # 돌 수 없다면
            break  # 탈출
        temp_dir = -temp_dir  # 해당방향과 반대로 돈다.
        minus -= 1  # 톱니바퀴 한개 증가

count = 0  # S의 개수 세기
for i in wheel:  # 톱니바퀴를 돈다.
    if i[0] == 1:  # 만약 12시방향 톱니바퀴가 S라면
        count += 1  # 해당 개수 증가
print(count)



# 14503 로봇 청소기 - bfs 느낌의 bf

n, m = map(int,input().split()) # N, M을 입력 받음

d =[[0] * m for _ in range(n)] # 청소 여부를 list로 생성
x, y, direction = map(int,input().split()) # x, y, direction를 입력 받음
d[x][y] = 1 # 현재 위치 청소 (0->1)

array = [] # 빈 칸, 벽을 입력 받음
for i in range(n): # n 개의 rows에 대해서 각 row의 입력을 받음
    array.append(list(map(int,input().split()))) # 입력은 list 형태로 array에 append

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 0: 위쪽 이동, 1: 오른쪽 이동, 2: 아래 이동, 3: 왼쪽 이동

def turn_left(): # 왼쪽으로 트는 함수
    global direction # global 함수 선언
    direction -= 1 # 왼쪽으로 이동
    # 0 : 북, 1 : 동, 2 : 남, 3 : 서
    if direction == -1: # 음수가 되는 경우, 
        direction = 3 # 3으로 초기화

count = 1 # 현재 위치를 청소 했음으로 1
turn_time = 0 # 왼쪽 방향으로 회전하는 횟수 계산, 4번인 경우 다른 조건 실행
while True:
    turn_left() # 왼쪽 방향으로 회전
    nx = x+ dx[direction] # 현재 방향으로 이동
    ny = y+ dy[direction] # 현재 방향으로 이동

    if d[nx][ny] == 0 and array[nx][ny] == 0: # 이동을 했는데, 방문하지 않았거나, 빈 공간인 경우
        d[nx][ny] = 1 # 이동한 위치에서 청소, 0->1
        x = nx # 위치 이동
        y = ny # 위치 이동
        count += 1 # 청소를 했음으로 1 증가
        turn_time = 0 # 왼쪽 방향 회전 횟수 0으로 초기화
        continue # 반복

    else: # 이동이 불가능 한 경우 왼쪽 방향 회전, 횟수 증가
        turn_time += 1

    if turn_time == 4: # 총 4번 회전 한 경우, 네 방향 모두 청소가 되어 있거나 벽이 있는 경우
        nx = x-dx[direction] # 바라보는 방향에서 뒤로 이동
        ny = y-dy[direction] # 바라보는 방향에서 뒤로 이동

        if array[nx][ny] == 0: # 이동한 위치가 벽이 아니라면,
            x = nx # 이동
            y = ny # 이동

        else: # 그렇지 않으면,
            break # 작동을 멈춤
        turn_time = 0 # 왼쪽 방향 회전 횟수 초기화

print(count) # count 값 출력



# 15685 드래곤 커브 - 이전 드래곤 커브 선을 거꾸로 확인하면서 90도 돌리며 추가해주면 된다. 는 아이디어... -> 현재 커브에 대한 방향 리스트


n = int(input())

graph = [[0] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n):

    y, x, d, g = map(int, input().split(' ')) # 리스트를 만들었을때, 주어진 y가 2차원 리스트의  인덱스임. 따라서 x y 바꿔줌
    graph[x][y] = 1 # 시작점 visited

    # 커브 리스트 만들기
    curve = [d]
    for j in range(g): # 세대만큼 반복
        for k in range(len(curve) - 1, -1, -1): # 커브 리스트 거꾸로 진행
            curve.append((curve[k] + 1) % 4) # 방향+1 하면서 커브 리스트 추가

    # 드래곤 커브 만들기
    for j in range(len(curve)): 
        x += dx[curve[j]] # 커브 리스트대로 방향 진행
        y += dy[curve[j]]
        if x < 0 or x >= 101 or y < 0 or y >= 101:
            continue
        graph[x][y] = 1 # 방문

answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1: # 오른쪽 밑 정사각형만을 모든 좌표에서 확인
            answer += 1

print(answer)


# 2290 LCD Test - 출력은 줄 단위로 해야하고, 함수는 숫자 단위로 쓰이면, 출력할 리스트를 만들고 완성한 후 리스트를 출력하는 방법을 씀

import sys
input = sys.stdin.readline

size, numbers = input().split()

size = int(size)

zero = list()
one = list()
two = list()
three = list()
four = list()
five = list()
six = list()
seven = list()
eight = list()
nine = list()

number_format = [zero, one, two, three, four, five, six, seven, eight, nine]
#인덱스를 이용해 해당 모양의 숫자를 찾음

zero.append(' '+'-'*size+' ') # 기징 상단
for _ in range(size): # size만큼
    zero.append('|'+' '*size+'|')
zero.append(' '*(size+2))
for _ in range(size): # size만큼
    zero.append('|'+' '*size+'|')
zero.append(' '+'-'*size+' ') # 기징 하단

one.append(' '*(size+2))
for _ in range(size):
    one.append(' '*(size+1)+'|')
one.append(' '*(size+2))
for _ in range(size):
    one.append(' '*(size+1)+'|')
one.append(' '*(size+2))

two.append(' '+'-'*size+' ')
for _ in range(size):
    two.append(' '*(size+1)+'|')
two.append(' '+'-'*size+' ')
for _ in range(size):
    two.append('|'+' '*(size+1))
two.append(' '+'-'*size+' ')

three.append(' '+'-'*size+' ')
for _ in range(size):
    three.append(' '*(size+1)+'|')
three.append(' '+'-'*size+' ')
for _ in range(size):
    three.append(' '*(size+1)+'|')
three.append(' '+'-'*size+' ')

four.append(' '*(size+2))
for _ in range(size):
    four.append('|'+' '*(size)+'|')
four.append(' '+'-'*size+' ')
for _ in range(size):
    four.append(' '*(size+1)+'|')
four.append(' '*(size+2))

five.append(' '+'-'*size+' ')
for _ in range(size):
    five.append('|'+(size+1)*' ')
five.append(' '+'-'*size+' ')
for _ in range(size):
    five.append(' '*(size+1)+'|')
five.append(' '+'-'*size+' ')

six.append(' '+'-'*size+' ')
for _ in range(size):
    six.append('|'+(size+1)*' ')
six.append(' '+'-'*size+' ')
for _ in range(size):
    six.append('|'+' '*(size)+'|')
six.append(' '+'-'*size+' ')

seven.append(' '+'-'*size+' ')
for _ in range(size):
    seven.append(' '*(size+1)+'|')
seven.append(' '*(size+2))
for _ in range(size):
    seven.append(' '*(size+1)+'|')
seven.append(' '*(size+2))

eight.append(' '+'-'*size+' ')
for _ in range(size):
    eight.append('|'+' '*(size)+'|')
eight.append(' '+'-'*size+' ')
for _ in range(size):
    eight.append('|'+' '*(size)+'|')
eight.append(' '+'-'*size+' ')

nine.append(' '+'-'*size+' ')
for _ in range(size):
    nine.append('|'+' '*(size)+'|')
nine.append(' '+'-'*size+' ')
for _ in range(size):
    nine.append(' '*(size+1)+'|')
nine.append(' '+'-'*size+' ')

for i in range(2*size+3):
    for number in numbers:
        print(number_format[int(number)][i]+' ', end='')
    print('')



# 16931 겉넓이 구하기 - 분류해서 해결하기. 6면의 겉넓이를 나눠서 

n, m = map(int, input().split())

a = []

for _ in range(n):
	a.append(list(map(int, input().split())))

b = n * m
t = n * m

no = 0
e = 0
w = 0
s = 0

for i in range(m):
	no += a[0][i]
	s += a[n-1][i]

for i in range(n):
	e += a[i][m-1]
	w += a[i][0]

for i in range(n-1):
	for j in range(m):
		if a[i][j] < a[i+1][j]:
			no += a[i+1][j] - a[i][j]

for i in range(n-1):
	for j in range(m):
		if a[n-i-1][j] < a[n-i-2][j]:
			s += a[n-i-2][j] - a[n-i-1][j]

for i in range(n):
	for j in range(m-1):
		if a[i][j] < a[i][j+1]:
			w += a[i][j+1] - a[i][j]


for i in range(n):
	for j in range(m-1):
		if a[i][m-j-1] < a[i][m-j-2]:
			e += a[i][m-2-j] - a[i][m-1-j]

print(no + e + w + s + t + b)
'''


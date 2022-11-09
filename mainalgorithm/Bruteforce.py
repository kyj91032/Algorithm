# 브루트포스 알고리즘: 완전 탐색

# 완전 탐색의 기본 동작 과정

1. 처음부터 끝까지 모두 확인(탐색)한다. for (1 ~ 3차원 선형탐색, 재귀, 최대최소갱신, 이동경로 정의, 비트마스크)
2. 주어진 조건을 제외하고, 불필요한 탐색을 줄일 가능성이 있는지 알아본다. if (탐색의 범위축소 ex) += 1 대신 += k, 백트래킹)
3. 부분 문제를 해결한다. def
+ 예시를 가지고 먼저 구현한 뒤 일반화 해나가기



# 3085 사탕게임 -> 부분 문제 해결 후 2차원 탐색

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
    for j in range(n): # 모든 경우 2차원 탐색해서 한번씩 바꿔보면서, check으로 연속된 개수 알아내서, answer에 최대값 저장
        if j + 1 < n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j] # 실제로 리스트를 바꾸는 방법.
            
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



# 6064 카잉달력 -> 답이 되는 값 자체를 1부터 선형 탐색, 탐색의 범위 축소 year += 1 을 year += M 으로

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



# 1107 리모컨 -> 최대최소갱신, 

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



# 나이트 움직이기 -> 좌표 이동경로(나이트의 8가지 이동) 정의 후 시뮬레이션

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



# 유닛의 자동 이동 -> 좌표 이동 경로 정의 후 시뮬레이션 + 방향 전환 함수(부분문제 해결)

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

	     

# 1917 정육면체 전개도 -> 첫 1을 밑면으로 시작해서 주사위를 dfs로 굴리면서(1은 연결되어 있음), dice의 모든 면이 1로 바뀌면, 전개도가 맞는거고 0이 하나라도 있으면, 전개도가 틀린 것.

import java.util.*;
import java.io.*;

public class Main{
    
    public static void main(String[] args) throws Exception{
        Solve solve = new Solve();
        solve.run();
    }
    
}

class Solve{
    
    private static class Cube{
        
        private int[] side;
        private int[] temp;
        private int foldCount;
         
        public Cube(){
            temp = new int[7];
            side = new int[7];
        }
        
        public boolean cubeCheck(){
            if(foldCount > 6) return false;
            for(int i = 1; i <= 6; i++) if(side[i] == 0) return false;
            return true;
        }
        
        public void setCube(int side){
            foldCount++;
            this.side[1] = side;
        }
        
        public void changeSide(int dir){
            if(dir == 1) doLeft();
            else if(dir == 2) doRight();
            else if(dir == 3) doDown();
            else if(dir == 4) doTop();
            tempToSide();
        }
        
        // 모든 변경 위치 초기화
        
        private void sideToTemp(){
            for(int i = 0; i <= 6; i++) temp[i] = side[i];
        }
        
        private void tempToSide(){
            for(int i = 0; i <= 6; i++) side[i] = temp[i];
        }
        
        private void doDown(){
            temp[1] = side[4];
            temp[4] = side[6];
            temp[5] = side[1];
            temp[6] = side[5];
            temp[2] = side[2];
            temp[3] = side[3];
        }
        
        private void doTop(){
            temp[1] = side[5];
            temp[4] = side[1];
            temp[5] = side[6];
            temp[6] = side[4];
            temp[2] = side[2];
            temp[3] = side[3];
        }
        
        private void doRight(){
            temp[1] = side[2];
            temp[2] = side[6];
            temp[3] = side[1];
            temp[6] = side[3];
            temp[4] = side[4];
            temp[5] = side[5];
        }
        
        private void doLeft(){
            temp[1] = side[3];
            temp[2] = side[1];
            temp[3] = side[6];
            temp[6] = side[2];
            temp[4] = side[4];
            temp[5] = side[5];
        }
        
    }
    
    private BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private String[] read;
    private int[] dy = {0, 0, 0, 1, -1};
    private int[] dx = {0, 1, -1, 0, 0};
    private int[] reverseDir = {0, 2, 1, 4, 3};
    private boolean[][] check;
    private int side;
        
    public void run(){
        for(int i = 0; i < 3; i++) System.out.println(validateCube(getArr()));
    }
    
    private String validateCube(int[][] arr){
        int sy = 0, sx = 0;
        for(int y = 0; y < 6; y++){
            for(int x = 0; x < 6; x++){
                if(arr[y][x] == 1){
                    sy = y;
                    sx = x;
                    break;
                }
            }
        }
        Solve.Cube cube = new Solve.Cube();
        validateCubeOperate(arr, cube, sy, sx);
        if(!cube.cubeCheck()) return "no";
        return "yes";
    }
    
    private void validateCubeOperate(int[][] arr, Cube cube, int y, int x){
        side++;
        cube.setCube(side);
        check[y][x] = true;
        for(int i = 1; i <= 4; i++){
            int ny = y + dy[i];
            int nx = x + dx[i];
            if(outOfBounds(ny, nx) || check[ny][nx] || arr[ny][nx] == 0) continue;
            cube.changeSide(i); // 정방향
            validateCubeOperate(arr, cube, ny, nx);
            cube.changeSide(reverseDir[i]); // 역방향으로 되돌림
        }
    }
    
    private boolean outOfBounds(int y, int x){
        return (y >= 6 || x >= 6 || y < 0 || x < 0);
    }
    
    private int[][] getArr(){
        int[][] ret = new int[10][10];
        check = new boolean[10][10];
        for(int i = 0; i < 6; i++){
            try{
                read = br.readLine().split(" ");
            } catch (IOException IOE) {}
            for(int j = 0; j < 6; j++) ret[i][j] = Integer.parseInt(read[j]);
        }
        return ret;
    }
    
}


# 16967 배열 복원하기 -> 분류해서 해결

h, w, x, y = map(int, input().split())
 
b = []
 
for _ in range(h+x):
	b.append(list(map(int, input().split())))
 
a = [[0] * w for _ in range(h)]
 
for i in range(x):
	for j in range(w):
		a[i][j] = b[i][j]
 
for i in range(y):
	for j in range(h):
		a[j][i] = b[j][i]
 
for i in range(h, x+h):
	for j in range(y, w+y):
		a[i-x][j-y] = b[i][j]
 
for i in range(w, y+w):
	for j in range(x, x+h):
		a[j-x][i-y] = b[j][i]
 
for i in range(x, h): # a를 순서대로 갱신하면, 옮겨도 겹치는 부분이 자연스럽게 해결됨.
	for j in range(y, w):
		a[i][j] = b[i][j] - a[i-x][j-y]
 
for i in range(h):
	print(*a[i])



# 20327 배열 돌리기6 -> 어떻게 분할해서 처리할건지.. 5 6 7 8번 연산은 1 2 3 4의 연산을 작은 2차원 리스트에서 연산을 다시 함으로서 만들 수 있음.

#include <iostream>
#include <string>
#include <cmath>
#include <set>
#include <unordered_map>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#define FIRST cin.tie(NULL); cout.tie(NULL); ios::sync_with_stdio(false);
#define MAX 150
#define INF 1e9

using namespace std;
int N, Q;
int A_Size;
int A[MAX][MAX];

void First_Operation(int L) {
	int Cnt = 0;
	int tmp[MAX][MAX];
	for (int i = 0; i < A_Size; i++) {
		for (int j = 0; j < A_Size; j++) {
			tmp[i][j] = A[i][j];
		}
	}
	for (int i = 0; i < A_Size; i += L) {
		for (int j = 0; j < A_Size; j += L) {
			int Y = i;
			int X = j;
			for (int k = Y; k < (Y + L); k++) {
				for (int l = X; l < (X + L); l++) {
					A[Y + L - 1 - k + (L * Cnt)][l] = tmp[k][l];
				}
			}
		}
		Cnt++;
		/*
			1번 예제에서 (2, 0)을 좌우 반전하면 (3, 0)이 되는데,
			A[(Y + L - 1) - k][l] = (1, 0)이 되므로, L을 1번 더해주어야
			(3, 0)이 된다. 이 L을 몇 번 더할 건지는 Cnt라는 변수가 정해준다.
		*/
	}
}

void Second_Operation(int L) {
	int Cnt = 0;
	int tmp[MAX][MAX];
	for (int i = 0; i < A_Size; i++) {
		for (int j = 0; j < A_Size; j++) {
			tmp[i][j] = A[i][j];
		}
	}
	for (int i = 0; i < A_Size; i += L) {
		for (int j = 0; j < A_Size; j += L) {
			int Y = i;
			int X = j;
			for (int k = Y; k < (Y + L); k++) {
				for (int l = X; l < (X + L); l++) {
					A[k][X + L - 1 - l + (L * Cnt)] = tmp[k][l];
				}
			}
			Cnt++;
		}
		Cnt = 0;
	}
}

void Third_Operation(int L) {
	int R = 0, C = 0, Cnt = 0;
	int tmp[MAX][MAX];
	for (int i = 0; i < A_Size; i++) {
		for (int j = 0; j < A_Size; j++) {
			tmp[i][j] = A[i][j];
		}
	}
	for (int i = 0; i < A_Size; i += L) {
		for (int j = 0; j < A_Size; j += L) {
			int Y = i;
			int X = j;
			for (int k = Y; k < (Y + L); k++) {
				for (int l = X; l < (X + L); l++) {
					A[l - (L * R) + (L * Cnt)][Y + L - 1 - k + (L * C)] = tmp[k][l];
				}
			}
			R++;
			C++;
		}
		Cnt++;
		R = 0;
		C = 0;
		/*
			마찬가지로 R, C라는 변수를 이용해서 범위 안에서만 회전하도록 해준다.
		*/
	}
}

void Fourth_Operation(int L) {
	int R = 0, C = 0, Cnt = 0;
	int tmp[MAX][MAX];
	for (int i = 0; i < A_Size; i++) {
		for (int j = 0; j < A_Size; j++) {
			tmp[i][j] = A[i][j];
		}
	}
	for (int i = 0; i < A_Size; i += L) {
		for (int j = 0; j < A_Size; j += L) {
			int Y = i;
			int X = j;
			for (int k = Y; k < (Y + L); k++) {
				for (int l = X; l < (X + L); l++) {
					A[X + L - 1 - l + (L * R)][k + (L * C) - (L * Cnt)] = tmp[k][l];
				}
			}
			C++;
		}
		Cnt++;
		R++;
		C = 0;
	}
}

void Fifth_Operation(int L) {
	First_Operation(A_Size); // 전체를 상하반전
	First_Operation(L); // 이후 부분만 다시 상하반전시킨다.
	// 결과적으로 부분을 유지한 채로 전체가 상하반전된다.
}

void Sixth_Operation(int L) {
	Second_Operation(A_Size); // 전체를 좌우반전
	Second_Operation(L); // 이후 부분만 다시 좌우반전시킨다.
	// 결과적으로 부분을 유지한 채로 전체가 좌우반전된다.
}

void Seventh_Operation(int L) {
	Third_Operation(A_Size); // 전체를 시계방향 90도 회전
	Fourth_Operation(L); // 이후 부분만 다시 반시계 방향으로 90도 회전
	// 결과적으로 부분을 유지한 채로 전체가 시계방향으로 90도 회전된다.
}

void Eighth_Operation(int L) {
	Fourth_Operation(A_Size); // 전체를 반시계방향 90도 회전
	Third_Operation(L); // 이후 부분만 다시 시계 방향으로 90도 회전
	// 결과적으로 부분을 유지한 채로 전체가 반시계방향으로 90도 회전된다.
}

int main() {
	FIRST
	cin >> N >> Q;
	A_Size = (1 << N);
	for (int i = 0; i < A_Size; i++) {
		for (int j = 0; j < A_Size; j++) {
			cin >> A[i][j];
		}
	}
	for (int i = 0; i < Q; i++) {
		int K, L;
		cin >> K >> L;
		int Len = (1 << L);
		if (K == 1) {
			First_Operation(Len);
		}
		else if (K == 2) {
			Second_Operation(Len);
		}
		else if (K == 3) {
			Third_Operation(Len);
		}
		else if (K == 4) {
			Fourth_Operation(Len);
		}
		else if (K == 5) {
			Fifth_Operation(Len);
		}
		else if (K == 6) {
			Sixth_Operation(Len);
		}
		else if (K == 7) {
			Seventh_Operation(Len);
		}
		else if (K == 8) {
			Eighth_Operation(Len);
		}
	}
	for (int i = 0; i < A_Size; i++) {
		for (int j = 0; j < A_Size; j++) {
			cout << A[i][j] << " ";
		}
		cout << "\n";
	}

	return 0;
}



# 20055 컨베이어 벨트 위의 로봇 -> 분할하여 해결, 자료구조의 활용. 굳이 리스트를 사용할 필요 없이, deque(queue)을 사용한다

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0]*n)
res = 0

while 1:
    belt.rotate(1)
    robot.rotate(1)
    robot[-1]=0 #로봇이 내려가는 부분이니 0

    if sum(robot): #로봇이 존재하면
        for i in range(n-2, -1, -1): #로봇 내려가는 부분 인덱스 i-1 이므로 그 전인 i-2부터 (먼저 올라간 로봇부터)
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1]>=1:
                robot[i+1] = 1
                robot[i] = 0
                belt[i+1] -= 1
        robot[-1]=0 #이 부분도 로봇 out -> 0임

    if robot[0] == 0 and belt[0]>=1:
        robot[0] = 1
        belt[0] -= 1
    res += 1
    if belt.count(0) >= k:
        break
                
print(res)


# 17413 단어 뒤집기2 -> 단어를 어떻게 부분 뒤집기 할건가.. 인덱싱과 temp로

import sys
word = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":       # 열린 괄호를 만나면
        i += 1 
        while word[i] != ">":      # 닫힌 괄호를 만날 때 까지
            i += 1 
        i += 1               # 닫힌 괄호를 만난 후 인덱스를 하나 증가시킨다
    
	elif word[i].isalnum(): # 숫자나 알파벳을 만나면
        start = i
        while i < len(word) and word[i].isalnum():
            i+=1
        tmp = word[start:i] # 숫자,알파벳 범위에 있는 것들을
        tmp.reverse()       # 뒤집는다
        word[start:i] = tmp
    
	else:                   # 괄호도 아니고 알파,숫자도 아닌것 = 공백
        i+=1                # 그냥 증가시킨다

print("".join(word))


	     
# 1676 팩토리얼 0의 개수 -> 팩토리얼의 값을 구하는 것 X, 5^n의 배수들의 개수의 누적 합으로 5의 배수 개수를 구한다. 5의 배수 개수가 0의 개수

#include <iostream>
using namespace std;

int main() {
    int ans = 0;
    
    int n;
    cin >> n;
    
    for (int i=5; i<=n; i*=5) # - 1~N까지의 숫자에서  5^1 = 5의 배수, 5^2 = 25의 배수, 5^3 = 125의 배수, 5^k이 n보다 작을 때 까지 이들의 개수를 구함.
			      # 이 개수는 N / 5^1 + N / 5^2 + N / 5^3 + ... 이런 방식으로 구할 수 있음.
        ans += n/i;
        
    cout << ans << '\n';
}


# 2004 조합 0의 개수 -> 1671의 일반화. 

#include <iostream>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
 
long long func(int n, int x)
{
	int num = 0;
 
	for (long long i = x; n / i >= 1; i *= x) {
		num += n / i;
	}
 
	return num;
}
 
int main(int argc, char *argv[])
{
	int n, m;
 
	long long five = 0;
	long long two = 0;
	
	cin >> n;
	cin >> m;
 
	five = func(n, 5) - func(n - m, 5) - func(m, 5);
	two = func(n, 2) - func(n - m, 2) - func(m, 2);
 
	cout << min(five, two) << endl;
 
	return 0;
}
'''

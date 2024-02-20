
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

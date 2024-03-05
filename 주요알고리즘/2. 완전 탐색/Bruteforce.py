'''
브루트포스 알고리즘: 완전 탐색

완전 탐색의 구현

1. 처음부터 끝까지 모두 탐색한다 -> 탐색하지 않아도 되는 부분을 찾으려는 접근
    for 1 ~ 3차원 선형탐색, 최대최소갱신, 
    재귀함수, 백트래킹, 순열과 조합,
    이동경로 정의, 0과1 테이블 정의 = 해시, 
    검색 시 정렬 해시 set dict 등의 이용,
    정렬 후 탐색, 이분탐색, 투포인터,
    완전 탐색의 범위가 너무 크면 이분탐색을 의심. target 값을 찾아야 하는 경우, 답을 mid로 가정하고 left, right를 갱신하며 mid를 찾아나간다.
'''

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

# 1917 정육면체 전개도 -> 첫 1을 밑면으로 시작해서 주사위를 dfs로 굴리면서(1은 연결되어 있음), dice의 모든 면이 1로 바뀌면, 전개도가 맞는거고 0이 하나라도 있으면, 전개도가 틀린 것.


# 20327 배열 돌리기6 -> 어떻게 분할해서 처리할건지.. 5 6 7 8번 연산은 1 2 3 4의 연산을 작은 2차원 리스트에서 연산을 다시 함으로서 만들 수 있음.


# 1676 팩토리얼 0의 개수 -> 팩토리얼의 값을 구하는 것 X, 5^n의 배수들의 개수의 누적 합으로 5의 배수 개수를 구한다. 5의 배수 개수가 0의 개수


# 2004 조합 0의 개수 -> 1671의 일반화. 


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

# 14499 주사위 굴리기 - 어떻게 주사위가 구르는 것을 구현하지?? -> 

# 인덱스 0부터 5까지 각각의 인덱스가 위쪽, 뒤쪽, 오른쪽, 왼쪽, 앞쪽, 바닥 이라고 했을 때
# [1, 2, 3, 4, 5, 6] => [3, 2, 6, 1, 5, 4] 로 변했음을 알 수 있다
# 마찬가지로 다른 방향으로 굴렸을 때에 대해서도 어떻게 변했는지를 알면 이 문제를 다 풀었다고 볼 수 있다.
# 이러한 규칙을 turn함수에 정의를 해놓고
# 굴려야 하는 타이밍에 함수를 실행시키면 된다.

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


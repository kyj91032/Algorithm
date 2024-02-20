import sys
input = sys.stdin.readline

while True:

    domino = []
    for i in range(1, 9):
        for j in range(i, 10):
            if i != j:
                domino.append([i, j])

    n = int(input())

    if n == 0:
        break

    grid = [[0] * 9 for _ in range(9)]

    for i in range(n):
        u, lu, v, lv = input().split()
        x1 = ord(lu[0]) - 65
        y1 = int(lu[1]) - 1
        grid[x1][y1] = int(u)
        x2 = ord(lv[0]) - 65
        y2 = int(lv[1]) - 1
        grid[x2][y2] = int(v)
        if [int(u), int(v)] in domino:
            domino.remove([int(u), int(v)])
        if [int(v), int(u)] in domino:
            domino.remove([int(v), int(u)])

    a, b, c, d, e, f, g, h, i = input().split()
    x = ord(a[0]) - 65
    y = int(a[1]) - 1
    grid[x][y] = 1
    x = ord(b[0]) - 65
    y = int(b[1]) - 1
    grid[x][y] = 2
    x = ord(c[0]) - 65
    y = int(c[1]) - 1
    grid[x][y] = 3
    x = ord(d[0]) - 65
    y = int(d[1]) - 1
    grid[x][y] = 4
    x = ord(e[0]) - 65
    y = int(e[1]) - 1
    grid[x][y] = 5
    x = ord(f[0]) - 65
    y = int(f[1]) - 1
    grid[x][y] = 6
    x = ord(g[0]) - 65
    y = int(g[1]) - 1
    grid[x][y] = 7
    x = ord(h[0]) - 65
    y = int(h[1]) - 1
    grid[x][y] = 8
    x = ord(i[0]) - 65
    y = int(i[1]) - 1
    grid[x][y] = 9
    

# 풀이 
    
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

turn = 1

while True:
    g = [[0] * 9 for _ in range(9)]
    n = int(input())

    if n == 0:
        break
    
    sudominoku = [] # 도미노 저장
    for i in range(1, 10):
        for j in range(i+1, 10):
            sudominoku.append((i, j))

    for _ in range(n): # 주어진 grid 채우기
        u, lu, v, lv = map(str, input().split())
        u = int(u)
        v = int(v)
        g[ord(lu[0])-65][int(lu[1])-1] = u
        g[ord(lv[0])-65][int(lv[1])-1] = v
        sudominoku.remove((min(u, v), max(u, v)))
    l = list(map(str, input().split()))

    for i, s in enumerate(l): # enumerate: 인덱스와 값을 동시에 가져옴
        g[ord(s[0])-65][int(s[1])-1] = i+1

    def check(x, y, tmp, g): # 겹치는 숫자 체크
        for i in range(9):
            if g[x][i] == tmp:
                return False
        for i in range(9):
            if g[i][y] == tmp:
                return False
        nx, ny = x//3 * 3, y//3 * 3
        for i in [nx, nx+1, nx+2]:
            for j in [ny, ny+1, ny+2]:
                if g[i][j] == tmp:
                    return False
        return True

    blank = [] # 비어있는 좌표 저장
    for i in range(9):
        for j in range(9):
            if g[i][j] == 0:
                blank.append((i, j))
    flag = 0 
    def go(g, sudominoku):
        global flag
        if len(sudominoku) == 0: # 도미노 다 썼으면 종료
            flag = 1
            print('Puzzle', turn)
            for u in range(9):
                for v in range(9):
                    print(g[u][v], end='')
                print()
            return
        if flag == 1: # 정답 찾았으면 종료
            return
        # 도미노 넣을 빈칸 탐색
        for i in range(9):
            for j in range(9):
                if g[i][j] == 0:
                    x, y = i, j
        # 빈칸에 모든 도미노 넣어봄
        for n1, n2 in sudominoku:
            # 도미노의 한칸을 빈칸에 두고 나머지 한칸은 상하좌우로 붙일 수 있음
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d] # 나머지 한칸 좌표
                # 스도쿠 판 벗어나면
                if nx < 0 or nx >= 9 or ny < 0 or ny >= 9:
                    continue
                # 빈칸이 아니면
                if g[nx][ny] != 0:
                    continue
                # tmp 배열 만들어서 빈칸에 넣을 도미노는 배열에서 뺌
                tmp = sudominoku[:]
                tmp.remove((n1, n2)) # 넣음
                # 겹치는 숫자 체크
                if check(x, y, n1, g) and check(nx, ny, n2, g): # 둘 다 겹치는 게 없으면
                	# 스도쿠 빈칸에 도미노 넣음
                    g[x][y], g[nx][ny] = n1, n2
                    # 정답 찾았으면 종료하기 위해
                    if flag == 1:
                        return
                    go(g, tmp)
                # 이 줄을 안넣어서 한참 헤맴.. 이 줄을 안넣으면 체크가 안된다.
                g[x][y], g[nx][ny] = 0, 0
                # n1, n2 바꿔서 넣는 경우 재귀 돌림
                tmp = sudominoku[:]
                tmp.remove((n1, n2))
                if check(x, y, n2, g) and check(nx, ny, n1, g):
                    g[x][y], g[nx][ny] = n2, n1
                    if flag == 1:
                        return
                    go(g, tmp)
                g[x][y], g[nx][ny] = 0, 0

    go(g, sudominoku)
    turn += 1

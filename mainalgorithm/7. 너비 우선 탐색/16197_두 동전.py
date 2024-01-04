# 16197 두 동전 - 방문처리가 필요 없음. 다시 돌아가는 탐색을 또 해도 count<10이라 시간복잡도 만족, 두개의 좌표에 대한 노드 (x1, y1, x2, y2)

from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    while queue:
        x1, y1, x2, y2, cnt = queue.popleft()

        if cnt >= 10:
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]

            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                # 벽이라면
                if board[nx1][ny1] == "#":
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == "#":
                    nx2, ny2 = x2, y2
                queue.append((nx1, ny1, nx2, ny2, cnt + 1))
            elif 0 <= nx1 < n and 0 <= ny1 < m:  # coin2가 떨어진 경우
                return cnt + 1
            elif 0 <= nx2 < n and 0 <= ny2 < m:  # coin1가 떨어진 경우
                return cnt + 1
            else:  # 둘 다 빠진 경우 무시
                continue

    return -1


if __name__ == "__main__":
    n, m = map(int, input().split())

    queue = deque()
    board = []
    temp = []
    for i in range(n):
        board.append(list(input().strip()))
        for j in range(m):
            if board[i][j] == "o":
                temp.append((i, j))

    queue.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0))

    print(bfs())

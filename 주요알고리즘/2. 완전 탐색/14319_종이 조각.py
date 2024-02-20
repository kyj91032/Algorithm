
# 14319 종이조각 - 비트마스킹

import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

paper = []
for _ in range(n):
	paper.append(list(map(int, input().rstrip())))

ans = []

for i in range(1 << n*m): # 2의 n * m승 가지의 경우의 수 모두 확인
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
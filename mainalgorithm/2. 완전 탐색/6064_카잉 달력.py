

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

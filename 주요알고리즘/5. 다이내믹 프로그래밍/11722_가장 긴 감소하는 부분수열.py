
# 11722 가장 긴 감소하는 부분수열 - i가 추가됨에 따라 점화식이 이전 i에 대해 뭘 요구하는지를 파악하는 과정에서, 이중 반복문이 필요했고, 시간복잡도까지 확인해주기(n < 1000)

n = int(input())

a = list(map(int, input().split()))

d = [1] * n # 사소한 초깃값 설정. d = [0]*n 으로 하면 틀림. 다른 반례에 걸려서..

d[0] = 1

for i in range(1, n):
	for j in range(i):
		if a[j] > a[i]:
			d[i] = max(d[i], d[j] + 1)
print(max(d))

	     
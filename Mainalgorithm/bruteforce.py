# 브루트포스 알고리즘: 완전 탐색

# 완전 탐색의 기본 동작 과정
'''
1. 처음부터 끝까지 모두 확인한다
'''

''' python

h = int(input()) # 시간 완전탐색. 86400개의 경우의 수. 3중 반복문 이용
cnt = 0
for i in range(n + 1):
	for j in range(60):
		for k in range(60):
			if '3' in str(i) + str(j) + str(k):
				cnt += 1
print(cnt)

'''

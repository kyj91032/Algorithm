# 2529 부등호

n = int(input())

l = list(input().split())

cnt = 1

s = []

def rec():
	k = len(s)
	global cnt, smax, smin # 전역 변수 선언
	
	if k >= 2:
		if l[k - 2] == '>':
			if s[k - 2] < s[k - 1]:
				return
		else:
			if s[k - 2] > s[k - 1]:
				return
	
	
	if len(s) == n + 1:
		smax = s[:] # 레퍼런스 고려. 복사할 때 인덱싱으로 해야 함
		if cnt == 1:
			smin = s[:]
			cnt = 0
		return
	
	for i in range(10):
		if i not in s:
			s.append(i)
			rec()
			s.pop()
	
rec()

print(''.join(str(x) for x in smax))
print(''.join(str(x) for x in smin))


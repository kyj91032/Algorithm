

# 1759 암호 만들기 - 백트래킹

l, c = map(int, input().split())
cl = list(input().split())

cl.sort()

mo = ['a', 'e', 'i', 'o', 'u'] # 모음 테이블. if in으로 모음인지 바로 판단 가능

s = []

def rec(start):
	if len(s) == l:
		m = 0
		n = 0
		for j in range(len(s)):
			if s[j] in mo: # 모음이면 출력하기
				m += 1
			else: n += 1
		if n >= 2 and m >= 1:
			print(''.join(map(str, s)))
			return
		else:
			return
  
	for i in cl[start:]:
		if i not in s:
			s.append(i)
			rec(cl.index(i) + 1)
			s.pop()
rec(0)
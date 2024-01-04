
# 6603 로또 - 리스트에서 오름차순 순열

q = []
def rec(start):
	if len(q) == 6: # 6개 오름차순 순열 출력
		print(' '.join(map(str, q)))
		return
	
	for i in s[start:]:
		if i not in q:
			q.append(i)
			rec(s.index(i) + 1)
			q.pop()

while 1:
	a = list(map(int, input().split()))
	if a == [0]:
		break
	
	k = a[0]
	s = a[1:]
	
	rec(0)
	print()


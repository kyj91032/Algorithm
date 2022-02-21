a, b, c = map(int, input().split())

i = 0
while 1:
	y1 = a + 15 * i
	y2 = (y1 - b) / 28
	if y2 % 1 == 0 and y2 > 0:
		y3 = (y2 - c) / 19
		if y3 % 1 == 0 and y3 > 0:
			print(int(y3))
			break
		else:
			i += 1
	else:
		i += 1

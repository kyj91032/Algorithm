
# 2290 LCD Test - 출력은 줄 단위로 해야하고, 함수는 숫자 단위로 쓰이면, 출력할 리스트를 만들고 완성한 후 리스트를 출력하는 방법을 씀

import sys
input = sys.stdin.readline

size, numbers = input().split()

size = int(size)

zero = list()
one = list()
two = list()
three = list()
four = list()
five = list()
six = list()
seven = list()
eight = list()
nine = list()

number_format = [zero, one, two, three, four, five, six, seven, eight, nine]
#인덱스를 이용해 해당 모양의 숫자를 찾음

zero.append(' '+'-'*size+' ') # 기징 상단
for _ in range(size): # size만큼
    zero.append('|'+' '*size+'|')
zero.append(' '*(size+2))
for _ in range(size): # size만큼
    zero.append('|'+' '*size+'|')
zero.append(' '+'-'*size+' ') # 기징 하단

one.append(' '*(size+2))
for _ in range(size):
    one.append(' '*(size+1)+'|')
one.append(' '*(size+2))
for _ in range(size):
    one.append(' '*(size+1)+'|')
one.append(' '*(size+2))

two.append(' '+'-'*size+' ')
for _ in range(size):
    two.append(' '*(size+1)+'|')
two.append(' '+'-'*size+' ')
for _ in range(size):
    two.append('|'+' '*(size+1))
two.append(' '+'-'*size+' ')

three.append(' '+'-'*size+' ')
for _ in range(size):
    three.append(' '*(size+1)+'|')
three.append(' '+'-'*size+' ')
for _ in range(size):
    three.append(' '*(size+1)+'|')
three.append(' '+'-'*size+' ')

four.append(' '*(size+2))
for _ in range(size):
    four.append('|'+' '*(size)+'|')
four.append(' '+'-'*size+' ')
for _ in range(size):
    four.append(' '*(size+1)+'|')
four.append(' '*(size+2))

five.append(' '+'-'*size+' ')
for _ in range(size):
    five.append('|'+(size+1)*' ')
five.append(' '+'-'*size+' ')
for _ in range(size):
    five.append(' '*(size+1)+'|')
five.append(' '+'-'*size+' ')

six.append(' '+'-'*size+' ')
for _ in range(size):
    six.append('|'+(size+1)*' ')
six.append(' '+'-'*size+' ')
for _ in range(size):
    six.append('|'+' '*(size)+'|')
six.append(' '+'-'*size+' ')

seven.append(' '+'-'*size+' ')
for _ in range(size):
    seven.append(' '*(size+1)+'|')
seven.append(' '*(size+2))
for _ in range(size):
    seven.append(' '*(size+1)+'|')
seven.append(' '*(size+2))

eight.append(' '+'-'*size+' ')
for _ in range(size):
    eight.append('|'+' '*(size)+'|')
eight.append(' '+'-'*size+' ')
for _ in range(size):
    eight.append('|'+' '*(size)+'|')
eight.append(' '+'-'*size+' ')

nine.append(' '+'-'*size+' ')
for _ in range(size):
    nine.append('|'+' '*(size)+'|')
nine.append(' '+'-'*size+' ')
for _ in range(size):
    nine.append(' '*(size+1)+'|')
nine.append(' '+'-'*size+' ')

for i in range(2*size+3):
    for number in numbers:
        print(number_format[int(number)][i]+' ', end='')
    print('')


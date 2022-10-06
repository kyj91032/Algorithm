# 반복과 재귀: loop가 필요한 알고리즘을 설계할 때, 반복문(iteration)과 재귀(recursion) 중 하나를 선택할 수 있다.

# 반복문의 기본 동작 과정

1. 초깃값이 존재해야 한다.
2. 반복 조건(= 종료 조건)을 설정하여 반복하는데, for은 횟수 조건(range), while은 상황 조건(if-break)이다.

+ 바텀 업으로 실행됨.

# 팩토리얼 반복 구현

result = 1
for i in range(1, n + 1):
  result *= i

print(result)



# 재귀 함수의 기본 동작 과정

1. 문제가 여러 개의 부분 문제로 쪼개지는지 확인한다.
2. 종료 조건을 설정하여 반복하는데 종료 조건을 만족하지 못할 때 재귀 호출이 일어나도록 한다.

+ 재귀함수가 쌓이는 것은 스택과 같다. 탑 다운으로 쌓이고 바텀 업으로 리턴됨.
재귀 호출은 스택에서 push로 해석할 수 있고, 종료 호출은 스택에서 pop으로 해석할 수 있다.
따라서 스택 자료구조를 활용해야 하는 상당수의 알고리즘은 재귀 함수를 이용해서 간편하게 구현될 수 있다. ex) DFS

# 팩토리얼 재귀 구현

def factorial_recursive(n):
  if n <= 1:
    return 1
  return n * factorial_recursive(n - 1)



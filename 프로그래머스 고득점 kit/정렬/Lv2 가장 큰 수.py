# 문자열의 정렬 순서
# 주어진 숫자를 문자열로 변환하여, 각 문자열을 3번 반복하여 비교한다. 이유는 1000이하의 숫자가 주어지기 때문에, 3자리수로 맞추어 비교하기 위함이다.
# 반복을 안하게되면 3과 30중에 3이 먼저 와야하는데 30이 먼저 오게된다.

def solution(numbers):
    
    numbers_str = [str(num) for num in numbers]
    numbers_str.sort(key=lambda num: num*3, reverse=True)

    return str(int(''.join(numbers_str)))


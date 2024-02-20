import sys
import math
input = sys.stdin.readline

N = int(input())

a = [False, False] + [True] * (N - 1) # 0, 1 제외하고 2 ~ N 까지 소수로 가정
prime_num = [] 

for i in range(2, N+1): # 에라토스테네스의 체 -> a[i]가 True이면 i는 소수
    if a[i]:
        prime_num.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False

answer = 0
left = 0
right = 0
while right <= len(prime_num):
    hap = sum(prime_num[left:right])
    if hap == N:
        answer += 1
        right += 1
    elif hap < N:
        right += 1
    else:
        left += 1

print(answer)


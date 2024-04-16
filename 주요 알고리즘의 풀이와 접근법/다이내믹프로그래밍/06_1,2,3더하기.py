# https://boj-helper.vercel.app/solve/9095?language=python

# 생각 과정
'''
이 문제는 그냥 다 적으면서 규칙을 알아내야함.
'''

# 풀이 코드
d = [0] * (11)

d[1] = 1 # 1
d[2] = 2 # 1+1, 2
d[3] = 4 # 1+1+1, 2+1, 1+2, 3
# 1+1+1+1, 2+1+1, 1+2+1, 1+1+2, 3+1, 1+3, 4

for i in range(4, 11):
    d[i] = d[i-1] + d[i-2] + d[i-3]

T = int(input())
for i in range(T):
    n = int(input())
    print(d[n])



# 피드백 후 정리
'''

'''
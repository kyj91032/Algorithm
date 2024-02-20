
# 11054 가장 긴 바이토닉 부분 수열 - 기준 인덱스의 좌측은 증가하는 부분수열, 우측은 감소하는 부분수열의 reverse를 구해서 합한 길이가 가장 긴 순간의 인덱스. 애초에 바이토닉을 한번에 구할 수가 없었다..

N = int(input())

List = list(map(int, input().split()))

dp1 = [1] * N
dp2 = [1] * N

sub_len = [0] * N

Max = 0

for i in range(N):
    for j in range(i):
        if List[i] > List[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
	  
	     
List.reverse()

for i in range(N):
    for j in range(i):
        if List[i] > List[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
dp2.reverse()

for i in range(N):
    sub_len[i] = dp1[i] + dp2[i]

print(max(sub_len) - 1)
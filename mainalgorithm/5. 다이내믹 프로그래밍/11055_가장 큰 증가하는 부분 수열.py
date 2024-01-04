
# 11055 가장 큰 증가 부분 수열 - 시간복잡도에 대해.. n이 10000까지는 이중 반복 가능성 있음

n = int(input())
	     
array = list(map(int, input().split()))

d = [1] * n
d[0] = array[0]
for i in range(1, n):
  for j in range(i): # 일차원 반복문으로 코드를 짜면, 앞 쪽이 고려되지 않는 걸 알 수 있는데, 이 때 n의 크기를 보고 이중 반복문을 활용할 생각을 해야함.
    if array[j] < array[i]:
      d[i] = max(d[i], d[j] + array[i]) # ai가 더 크면 이전 d에 넣어보고
    else:
      d[i] = max(d[i], array[i]) # ai가 더 작으면 ai만 넣어보고

print(max(d))
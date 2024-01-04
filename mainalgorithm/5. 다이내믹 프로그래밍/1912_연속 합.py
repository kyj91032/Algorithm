
# 1912 연속 합 - if를 써야할까 max()로 충분할까?

n = int(input())

arr = list(map(int, input().split()))
dp = [0] * len(arr)
dp[0] = arr[0]

for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i-1] + arr[i]) # 점화식 : max(i번째 수를 선택 안함, i번째 수를 선택함)

print(max(dp))

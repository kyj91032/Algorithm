import sys
input = sys.stdin.readline

n, s = map(int, input().split())

a = list(map(int, input().split()))

left = 0
right = 0
length = 100001
hap = a[0] # 누적 합을 사용하는 이유 : 부분합을 구할 때, 누적합을 사용하면 O(1)의 시간복잡도로 구할 수 있기 때문
# sum()을 사용하면 O(n)의 시간복잡도가 걸린다. -> 반복문 + sum()을 사용하면 O(n^2)의 시간복잡도가 걸린다.


while left <= right:
    if hap >= s:
        length = min(length, right-left+1)
        hap -= a[left]
        left += 1
    elif hap < s:
        right += 1
        if right < n:
            hap += a[right]
        else:
            break
        

if length == 100001:
    print(0)
else:
    print(length)


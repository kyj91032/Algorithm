'''
input의 최대길이가 지나치게 길고, 특정 값을 찾아야 하는 문제라면 이분탐색을 의심
target 값을 찾아야 하는 경우, 중간값으로 가정하고 left, right를 갱신하며 mid를 찾아나간다.
'''

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # 중간 값이 타겟과 일치하는지 확인
        if arr[mid] == target:
            return mid
        # 중간 값이 타겟보다 큰 경우, 오른쪽 절반 탐색
        elif arr[mid] > target:
            right = mid - 1
        # 중간 값이 타겟보다 작은 경우, 왼쪽 절반 탐색
        else:
            left = mid + 1
    
    # 타겟을 찾지 못한 경우
    return -1

# 테스트
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(arr, target)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")

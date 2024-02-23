'''
1. 모든 time에 대해 1~max(times)*n까지의 시간을 완전탐색으로 찾는다?
2. 범위가 너무 큼
3. 이분탐색 의심
'''

def solution(n, times):
    # time을 찾기 위한 이분탐색
	# 가능한 최솟값과 최댓값을 left와 right로 설정
    left = 1
    right = max(times) * n
    
    # 이분탐색이니 left가 right 이하인 동안
    while left <= right:
    	# 가운데 : 더하고 2로 나눈 몫(정수)
        mid = (left+right)//2
        # 심사한 사람 수 : 누적 변수
        people = 0
     	
        # time이 mid라고 가정했을 때, 각 심사대에서 심사할 수 있는 사람 수를 구하는 것임
        for time in times:
        	# 해당 심사대에서 주어진 시간동안 심사 받은 수 더하기
            people += mid//time 
            
            # 중간에라도 이미 n명보다 많이 심사했다면 break
            if people >= n:
                break
        # n명 초과 심사했다면, 시간이 너무 많은 것
        # 딱 n명 심사했더라도, 시간이 남을 가능성 있음
        if people >= n:
            answer = mid
            right = mid -1
        # n명 미만 심사했다면, 시간이 너무 부족하다
        else :
            left = mid + 1
    return answer

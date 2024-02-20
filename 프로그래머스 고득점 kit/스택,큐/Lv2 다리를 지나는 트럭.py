from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    time = 0
    ing = deque([0] * bridge_length) # 다리 위 트럭
    truck_weights = deque(truck_weights) # 대기 트럭
    
    truck_weights_ing = 0 # 다리 위 트럭 무게
    # sum을 쓰면 시간 초과가 남 for+sum은 O(n^2)이기 때문에 -> 누적 합을 사용

    while ing: # ing이 비어있지 않으면 계속 반복
        truck_weights_ing -= ing.popleft() # 다리 위 트럭 무게에서 빠져나온 트럭 무게 빼기
        time += 1
        
        if truck_weights:
            if truck_weights_ing + truck_weights[0] <= weight:
                truck_weights_ing += truck_weights[0]
                ing.append(truck_weights.popleft())
            else:
                ing.append(0)

    return time
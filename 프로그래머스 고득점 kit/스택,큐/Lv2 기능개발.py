# time만 분리해서 증가시키면서 100이 되면 pop하는 것이 핵심 아이디어
# 100 넘은 것들은 계속 pop하고, 100이 안넘으면 time을 증가시키면서 100이 넘는지 확인하며 100이 넘으면 쌓인 count를 답에 추가하게 됨

# 어떻게 큐를 이용해서 풀어야한다는 것을 알 수 있을까??? 

def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0 # 배포되는 기능의 수
    
    while len(progresses)> 0: # progresses를 다 pop하면서 반복
        if (progresses[0] + time*speeds[0]) >= 100: # 100이면 pop, 그리고 count += 1
            progresses.pop(0)
            speeds.pop(0)
            count += 1            
        else: # 100이 아니라면
            if count > 0: # 이전에 쌓인 count가 있다면 answer에 추가하고 count 초기화
                answer.append(count)
                count = 0
            time += 1 # time은 100이 아닌경우 계속 증가
    answer.append(count)
    return answer

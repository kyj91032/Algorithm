def solution(number, k):
    answer = [] # Stack

    '''
    1. number를 순회하면서
    2. answer의 마지막 원소가 현재 원소보다 작으면 pop하고 k -= 1
    3. answer에 현재 원소를 append
    4. k가 0이 되면 종료
    '''
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k]) # k가 0이 아닌 경우 예외처리 예를들어 443332211같은 수가 내려가는 경우는 k가 남음

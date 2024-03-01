from collections import defaultdict
def solution(friends, gifts):
    k = len(friends) # 친구 수
    
    answer_list = [0 for _ in range(k)] # 친구 별 다음달 받을 선물 수
    
    # 선물 지수만 계산
    '''
    defaultdict를 이용해 gifts를 돌면서 선물지수 계산만이 아닌 표까지 만들 수 있는 것.
    friends를 두개씩 조합할 필요도 없어짐
    '''
    rate = defaultdict(int) # defaultdict은 키가 없을 때 자동으로 디폴트 값을 생성해준다. int는 0을 생성해준다.
    
    # 인덱스랑 벨류값
    idx_record = dict() # 빈 딕셔너리 생성
    value_record = dict()
    
    # 표를 만들자
    chart = [[0] * k for _ in range(k)] # 2차원 배열 생성. 친구 수 x 친구 수 만큼의 0으로 채워진 배열을 만든다.
    
    for i in range(k):
        for j in range(k):
            if i == j:
                chart[i][j] = -1 # 자기 자신은 -1로 채워준다.
    
    # 순서를 정해주자
    for idx, value in enumerate(friends):
        idx_record[value] = idx # 친구마다 인덱스를 매핑 -> 인덱스로 chart를 찾기 위해
        value_record[idx] = value # 인덱스마다 친구를 매핑 -> 선물 지수 비교를 위해. 이름으로 rate를 찾기 위해
        
    for gift in gifts:
        giver, receiver = gift.split() # 선물을 주는 사람, 받는 사람
        
        # 선물 지수 계산
        rate[giver] += 1
        rate[receiver] -= 1
        
        # 표 제작
        idx_giver = idx_record[giver] # 선물을 주는 사람의 인덱스
        idx_receiver = idx_record[receiver] # 선물을 받는 사람의 인덱스
        # 를 이용해서 차트 표를 완성한다.
        chart[idx_giver][idx_receiver] +=1
        chart[idx_receiver][idx_giver] -=1
        
    for c in range(k):
        for i in range(k):
            if chart[c][i] > 0: # 준게 더 많으면
                answer_list[c] += 1
            if chart[c][i] == 0: # 같으면 선물 지수 비교
                a = value_record[c] 
                b = value_record[i] 
                if rate[a] > rate[b]:
                    answer_list[c] += 1
    return max(answer_list)

'''
8자 그래프: 진입차수와 진출차수가 각각 2개 이상인 그래프
막대 그래프: 진입차수가 0이고 진출차수가 2개 이상인 그래프
도넛 그래프: 나머지 그래프

그래프라고 해서 무조건 dfs/bfs가 아니라 그래프의 특징을 파악해서 푸는 문제
'''

def solution(edges):
    answer = [0,0,0,0] # 최초노드 번호, 막대, 8자, 도넛
    
    # 진출차수와 진입 차수 초기화 및 카운팅
    # dict로 노드번호와 진입차수, 진출차수를 매핑해서 저장
    indegree = {}
    for a,b in edges:
        if not indegree.get(a): # get을 이용해 키가 없으면 초기화
            indegree[a] = [0,0] # 진입차수, 진출차수
        if not indegree.get(b): # get을 이용해 키가 없으면 초기화
            indegree[b] = [0,0] # 진입차수, 진출차수
        
        indegree[a][0] += 1 # 진입차수+1
        indegree[b][1] += 1 # 진출차수+1
    
    # 최초 점: 진입차수가 없고 진출 차수가 2이상
    # 막대 : 진입차수 있고 진출 차수 없음
    # 8자 그래프 : 진입차수 진출차수 각각 2개이상
    # 도넛: 나머지 그래프
    for key, i in indegree.items(): # key는 노드번호, i는 진입차수, 진출차수
        # 최초점
        if i[0] >= 2 and i[1] == 0: # 진입차수가 2이상이고 진출차수가 0이면
            answer[0] = key
        # 막대
        elif i[0] == 0 and i[1] > 0: # 진입차수가 0이고 진출차수가 2이상이면
            answer[2] +=1 # 막대 그래프 카운팅
        # 8자
        elif  i[0] >= 2 and i[1] >=2: # 진입차수가 2이상이고 진출차수가 2이상이면
            answer[3] += 1 # 8자 그래프 카운팅
            
    answer[1] = (indegree[answer[0]][0] - answer[2] - answer[3])

    return answer

'''
단어변환 문제처럼 bfs일 것 같음
근데 목표 탐색 깊이가 정해져 있음!!
이것만으로도 dfs가 효과적일 확률 높음
'''

def solution(tickets):
    answer = []
    
    '''
    출발지로 현재위치를 생각하면 안됨
    현재위치를 초기값으로 주고, 출발지와 비교하며 탐색해야함
    '''

    visited = [False] * len(tickets) # 티켓 마다 방문(사용) 여부 테이블
    
    def dfs(airport, path): # airport는 현재 위치, path는 지금까지 사용한 티켓들의 경로
        if len(path) == len(tickets)+1: # path가 티켓 수+1이면(모든 티켓을 사용했으면) 탐색 다했다는 뜻이므로 return : 종료조건!!!
            answer.append(path) # 도착하는 모든 경우가 담긴다.
            return
        
        for idx, ticket in enumerate(tickets): # 모든 티켓을 순회하며 = 모든 노드에서 dfs를 수행
            if airport == ticket[0] and visited[idx] == False: # 현재 위치와 출발지가 같고, 사용하지 않은 티켓이면
                visited[idx] = True # 방문처리(사용처리)
                dfs(ticket[1], path+[ticket[1]]) # 도착지 기준으로 다시 dfs
                visited[idx] = False # 백트래킹(사용처리 해제) : 다른 경로에서 visited를 사용할 수 있도록
        
    dfs("ICN", ["ICN"])
    
    answer.sort() # 도착하는 모든 경우를 담은 answer를 정렬

    return answer[0] # 알파벳 순서가 앞서는 경로를 리턴

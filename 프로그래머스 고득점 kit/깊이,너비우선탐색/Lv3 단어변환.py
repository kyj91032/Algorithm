'''
왜 bfs인가?
1. 일단 탐색은 맞음
2. 그럼 bf인가? 접근하기 힘듦
3. 탐색하는 과정을 보니 이전 결과를 이어받아 계속 탐색해감
4. dfs/bfs나 dp일 수도 있다는 생각
5. 최소 단계로 도달해야한다는 점에서 bfs라는 힌트 얻을수있고, 단어 수 차이가 1인 것들을 큐에 넣으면서 탐색해가면 된다는 것 알 수 있음
'''

from collections import deque

def solution(begin, target, words):
    
    if target not in words : 
        return  0
    
    return bfs(begin, target, words)

def bfs(begin, target, words):

    queue = deque()
    queue.append([begin, 0]) #시작 단어와 단계 0으로 초기화
    
    while queue:
        now, step = queue.popleft()
        
        if now == target: # target이면 바로 리턴
            return step
        
        # 단어를 모두 체크하면서, 해당 단어가 변경될 수 있는지 체크
        for word in words:
            count = 0
            for i in range(len(now)): #단어의 길이만큼 반복하여
                if now[i] != word[i]: #단어에 알파벳 한개씩 체크하기
                    count += 1
                    
            if count == 1: 
                queue.append([word, step+1]) # 한개 차이인 경우, 큐에 추가

            '''
                근데 이렇게 하면 중복 탐색이 생기지 않나?
                => 초반에 생길 수 있지만 결국 now == target에서 바로 리턴해서 빠저나옴. 
                복잡도 문제는 없는듯
            '''

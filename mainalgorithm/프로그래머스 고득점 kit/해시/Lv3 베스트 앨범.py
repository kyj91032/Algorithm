def solution(genres, plays):
    answer = []

    songMap3 = [[genres[i], plays[i], i] for i in range(len(genres))]
    songMap3 = sorted(songMap3, key=lambda x: (-x[1], x[2])) # 재생수 내림차순, 고유번호 오름차순 정렬

    genre_play = {} # 장르별 재생수

    for a in songMap3:
        if a[0] not in genre_play:
            genre_play[a[0]] = a[1]
        else:
            genre_play[a[0]] += a[1]
    
    genre_play = sorted(genre_play.items(), key=lambda x: -x[1]) # 장르별 재생수 내림차순 정렬

    for i in genre_play:
        cnt = 0
        for j in songMap3:
            if i[0] == j[0]: # 장르가 같으면
                cnt += 1
                if cnt > 2:
                    break
                else: # 
                    answer.append(j[2])

        # 이중 반복문으로 다 돌아도 장르 종류는 < 100, 장르와 재생횟수는 <10,000 이므로 O(N^2)으로도 충분히 가능
        # 그래서 노래가 1개일 경우를 따로 분기하지 않고 매 장르마다 반복문을 끝까지 돌면서 어차피 한개만 들어가도록 되어있음.
                    
    return answer
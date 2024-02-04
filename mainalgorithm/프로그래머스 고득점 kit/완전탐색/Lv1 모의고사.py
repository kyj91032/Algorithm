def solution(answers):
    
    a = [1,2,3,4,5] * 2000
    b = [2,1,2,3,2,4,2,5] * 2000
    c = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    score = [0, 0, 0]
    for ai, bi, ci, ans in zip(a, b, c, answers):
        if ai == ans:
            score[0]+=1
        if bi == ans:
            score[1]+=1
        if ci == ans:
            score[2]+=1
    
    result = []
    for i in range(len(score)): # 최댓값 이면 result에 추가
        if score[i] == max(score):
            result.append(i+1)
    
    return result
    

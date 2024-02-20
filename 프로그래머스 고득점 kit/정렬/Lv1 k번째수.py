def solution(array, commands):
    
    answer = []
    
    for cmd in commands:
        i = cmd[0]
        j = cmd[1]
        k = cmd[2]
        newArr = sorted(array[i-1:j])
        answer.append(newArr[k-1])
    
    return answer
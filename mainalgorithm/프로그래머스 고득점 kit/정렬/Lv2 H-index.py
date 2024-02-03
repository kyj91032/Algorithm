def solution(citations):
    n = len(citations)
    c = sorted(citations)
    
    for i in range(n):
        if c[i] >= n - i: # c[i]값 보다 이상일 필요가 없다. c[i]값은 오른쪽 길이 값보다 크기만 하면 된다.
            return n - i
            
    return 0
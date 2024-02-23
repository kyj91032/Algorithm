def solution(n, lost, reserve):
    
    lost.sort()
    
    for i in lost[:]: # 리스트의 변경사항을 바로 적용하기 위해 [:]로 복사본을 만들어서 사용
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
    
    student = [1] * n
    for l in lost:
        student[l-1] = 0
    print(student)
    for l in lost:
        if l - 1 in reserve and student[l-1] == 0:
            reserve.remove(l-1)
            student[l-1] = 1
        if l + 1 in reserve and student[l-1] == 0:
            reserve.remove(l+1)
            student[l-1] = 1    

    answer = sum(student)
    print(student)
    return answer
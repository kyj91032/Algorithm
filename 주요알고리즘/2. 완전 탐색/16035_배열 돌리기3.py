
# 16035 배열 돌리기3 - arr을 바로 바꾸기보단 함수 쓰고 tmp에 담아서 arr에 넣어 바꾸기

import sys
input=sys.stdin.readline

def cal1(arr):
    temp=[[0]*m for _ in range(n)]
    for i in range(n):
        temp[i]=arr[n-i-1]
    return temp
def cal2(arr):
    temp=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j]=arr[i][m-j-1]
    return temp
def cal3(arr,n,m):
    temp=[[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j]=arr[n-j-1][i]
    return temp
def cal4(arr,n,m):
    temp=[[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j]=arr[j][m-i-1]
    return temp
def cal5(arr):
    temp=[[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            temp[i][j+m//2]=arr[i][j]
    for i in range(n//2):
        for j in range(m//2,m):
            temp[i+n//2][j]=arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2,m):
            temp[i][j-m//2]=arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2):
            temp[i-n//2][j]=arr[i][j]
    return temp
def cal6(arr):
    temp=[[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            temp[i+n//2][j]=arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2):
            temp[i][j+m//2]=arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2,m):
            temp[i-n//2][j]=arr[i][j]
    for i in range(n//2):
        for j in range(m//2,m):
            temp[i][j-m//2]=arr[i][j]
    return temp

n,m,r=map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(n)]
cals=list(map(int, input().split()))

for cal in cals:
    if cal==1:
        arr=cal1(arr)
    elif cal==2:
        arr=cal2(arr)
    elif cal==3:
        arr=cal3(arr,n,m)
        n,m=m,n
    elif cal==4:
        arr=cal4(arr,n,m)
        n,m=m,n
    elif cal==5:
        arr=cal5(arr)
    else:
        arr=cal6(arr)

for i in arr:
    print(*i)


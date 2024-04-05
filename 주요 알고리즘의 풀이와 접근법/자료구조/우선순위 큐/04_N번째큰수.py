# https://boj-helper.vercel.app/solve/2075?language=python

# 생각 과정
'''
처음에 두가지 풀이를 시도했다.
첫번째는 리스트에서 정렬하고 5번째 인덱스를 출력하는 방법이었다. 시간복잡도 O(nlogn)
두번째는 우선순위 큐를 사용해서 5번째 큰 수를 출력하는 방법이었다. 시간복잡도 O(nlogn)
사실 둘이 똑같네 .. 
-> 둘다 메모리 초과가 났다.

=> 우선순위 큐의 크기를 정하고 (고정시키고) 원소들을 돌린다.
=> 우선순위 큐가 최대, 최소를 구하는데에 최적화된 역할 + 큐로서의 역할을 모두 수행한다.
'''

# 풀이 코드
import heapq

n = int(input())

pq = [] # 크기를 n으로 고정. n번째 큰 수니까 마지막에 큐에서 pop하면(그 큐 안에서의 최솟값) n번째 큰 수가 나오도록 함. => 메모리 초과 해결

for i in range(n):
    tmp = list(map(int, input().split()))
    for e in tmp:
        if len(pq) == n: # 큐의 크기가 n이면
            if e > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, e)
        else:
            heapq.heappush(pq, e)

print(pq[0])


# 피드백 후 정리
'''
1. 우선순위 큐는 리스트를 선언하고, 그 리스트에 힙 연산(heappush, heappop)을 수행함으로써 구현하는 것이다.
   그렇기 때문에 리스트의 pq[0]은 최솟값을 가르키게 된다.
2. 우선순위 큐도 결국 큐이기 때문에 크기를 조절하여 적절히 push와 pop을 할 수 있어야 한다.
'''
#대표적인 큐 구현 문제!!

import sys
from collections import deque
n, k= map(int, input().split())

dq = deque(list(range(1, n+1))) #1~n까지 덱 자료구조

while dq: #dq가 완전히 빌 때 멈춘다.
    for _ in range(k-1):
        cur = dq.popleft() 
        dq.append(cur)
    dq.popleft() #k=3번째는 그냥 사라져버리기
    
    if len(dq)==1:
        print(dq[0])
        break
    
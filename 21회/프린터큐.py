from collections import deque
import sys
input = sys.stdin.readline
l=int(input())
for _ in range(l):
    n, m = map(int, input().split())
    #n : 문서의 개수
    #myQueue에서 m번째로 놓인 문서가 몇번쨰로 인쇄 됐는지 출력
    lst = list(map(int, input().split()))
    myQueue = deque()
    for i,x in enumerate(lst):
        myQueue.append((i,x))
    lst.sort( ) #오름차순 
    cnt = 0
    while myQueue:
        i,x  = myQueue.popleft()
        if x == lst[-1]: #왼쪽으로 뽑아낸 게 가장 중요도가 높다면
            lst.pop()
            cnt+=1#인쇄가 될 때마다 cnt값은 1씩 증가
            if i== m: #만약 그 뽑아 낸 인덱스가 m과 같다면 정답 출력
                print(cnt)
                break
            
        else: #왼쪽으로 뽑아낸 게 중요도가 가장 높은 게 아닐 때
            myQueue.append((i,x)) 
                 
    
    
    
    
        
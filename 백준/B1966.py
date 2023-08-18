from collections import deque
k = int(input()) #테스트 케이스 개수


for _ in range(k): #테스트 케이스 개수
    n , m= map(int, input().split())
    #n: 문서의 개수, m: 궁금한 문서의 현재 위치
    paper = list(map(int, input().split()))
    myDeque = deque()
    
    for i,x in enumerate(paper):
        myDeque.append((i,x))
    paper.sort()
    cnt=0   
    while myDeque:
        
        i,x = myDeque.popleft()
        if x != paper[-1]:
            myDeque.append((i,x))
        else:
            paper.pop()
            cnt+=1
            if i==m:
                print(cnt)
    
    
    
        





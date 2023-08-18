from collections import deque

n, limit = map(int, input().split())
p= list(map(int, input().split()))

p.sort()
p=deque()
cnt=0 
while p: #boat가 비어있을 때까지
    if len(p)==1:
        cnt+=1
        break
    if p[0]+p[-1]>limit:
        p.pop() #가장 무거운 사람 pop시킴
        cnt+=1
        
    else:
        p.popleft()
        p.pop()
        cnt+=1
        
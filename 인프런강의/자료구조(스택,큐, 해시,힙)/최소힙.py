import heapq as hq

a= []
while True:
    n= int(input())
    if n==-1:
        break
    if n ==0 :
        if len(a)==0: #만약 비어있다면
            print(-1) #-1 출력
        else: #비어있지 않다면 루트 노드 값 출력
            print(hq.heappop(a))
    else:
        hq.heappush(a, n) #a라는 리스트에 n값을 push
                
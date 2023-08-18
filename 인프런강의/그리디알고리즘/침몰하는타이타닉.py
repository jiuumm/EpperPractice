
n,limit= map(int, input().split())
boat = list(map(int, input().split()))
boat.sort()
cnt=0 
while boat: #boat가 비어있을 때까지
    if len(boat)==1:
        cnt+=1
        break
    if boat[0]+boat[-1]>limit:
        boat.pop() #가장 무거운 사람 pop시킴
        cnt+=1
        
    else:
        boat.pop(0)
        boat.pop()
        cnt+=1
        
        
    

     

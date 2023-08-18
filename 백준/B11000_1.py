
n=int(input())
time = []
for i in range(n):
    s,e = map(int, input().split())
    time.append((s,e))
time.sort(key=lambda x: (x[1],x[0]))
#end time을 기준으로 오름차순으로 정렬
endTime = 0
res=0
tmp=[]
while time:
    if len(time)==1:
        res+=1
        break
    
    for s,e in time:
        if s>=endTime:
            endTime= e
            res+=1
            time.remove((s,e))
            

print(res)             


            
from collections import deque
n=int(input())
time = []
for i in range(n):
    s,e = map(int, input().split())
    time.append((s,e))
time.sort(key=lambda x: (x[1],x[0]))
#end time을 기준으로 오름차순으로 정렬

timeManager = deque()
for s,e in time:
    timeManager.append((s,e))

endTime = 0
cnt=0

while time:
    if len(time)==1:
        cnt+=1
        break
    for s,e in time:
        if s>= endTime:
            endTime=e
            cnt+=1
            time.pop()
        print(time)

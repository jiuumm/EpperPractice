#회의실 배정
#회의가 끝나는 시점을 기준으로 정렬해야 한다.

n= int(input())
meeting=[]
for i in range(n):
    s,e = map(int, input().split())
    meeting.append((s,e))
'''
key값을 기준으로 정렬된다.
<list>.sort(key=<function>, reverse = <bool>)

'''   
meeting.sort(key=lambda x : (x[1], x[0]) )
endtime = 0
res=0
for s, e in meeting:
    if s>=endtime:
        endtime = e
        res+=1
        
print(res)
        
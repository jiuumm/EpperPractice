
import sys
input= sys.stdin.readline

n= int(input())
s = list(map(int, input().split()))
e = list(map(int, input().split()))

#가장 먼저, 미팅 시간을 튜플형태로 담는다.
meeting = []
for i in range(n):
	meeting.append((s[i], e[i]))

meeting.sort(key = lambda x: (x[1], x[0]))


endTime = 0
cnt= 0

e1=e2 = -1
 #이 for문이 도대체 이해가 안간다....ㅎ
for now_s,now_e in meeting:
	if e1<= now_s:
		e1 = now_e
		cnt+=1
	elif e2<=now_s:
		e2 = e1
		e1 = now_e
		cnt+=1
	
print(cnt)

			
		
	
		

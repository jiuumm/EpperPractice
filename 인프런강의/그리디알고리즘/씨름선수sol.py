n=int(input())
body=[]
for i in range(n):
    a,b = map(int, input().split())
    body.append((a,b))#튜플 형태로 append
body.sort(reverse=True) #첫번째 자료를 내림차순으로 정리
largest = 0

cnt=0
for x,y in body: #x,y = 키, 몸무게
    if y>largest:
        cnt+=1
        largest=y
        
print(cnt)
    

    
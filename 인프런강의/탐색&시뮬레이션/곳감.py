n= int(input()) #판: n*n
A = [list(map(int, input().split())) for _ in range(n)]
m= int(input()) #명령의 개수

#Q. 리스트는 스택인가?
#2(행번호) 0(왼쪽 ? 오른쪽? ) 3(이동수)
for i in range(m):#명령
    #개수만큼 반복
    #배열에 저장하지 않고 그냥 바로 처리한다.
    h ,t, k =map(int, input().split())
    if t==0: #왼쪽회전일때
        for _ in range(k): #이동 횟수 반복
            A[h-1].append(A[h-1].pop(0))   
    else: #오른쪽 회전일 때
        for _ in range(k) :
            A[h-1].insert(0, A[h-1].pop()) #맨 뒤에 것을 pop해서
            #맨 앞에 insert하라!
s=0
e= n-1
sum=0
for i in range(n):
    for j in range(s, e+1):
        sum+=A[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
        
                   
                
print(sum)           
            
            
        
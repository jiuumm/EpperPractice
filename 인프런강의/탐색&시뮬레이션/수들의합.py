#투포인터 문제!
#n= 리스트 원소 개수
# m= 목표 합
n, m= map(int, input().split())
A= list(map(int, input().split()))

p1=0
p2=1
cnt=0
sum=0
while p2<n:#p2: 0~n-1
    if sum==m:
        cnt+=1
        p2+=1
    elif sum>m:
        sum-=A[p1]
        p1+=1
    else: #sum<m:
        p2+=1
        sum+=A[p2]

print(cnt)
        
        


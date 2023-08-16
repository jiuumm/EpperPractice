#sort방법 말고 O(n)으로 끝낼 수 있는 방법
n= int(input())
a= list(map(int, input().split()))
m = int(input())
b= list(map(int, input().split()))

p1=p2=0
c=[]
while p1<n and p2<m: #하나의 리스트가 다 처리될때까지
    if a[p1]<= b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
        
if p1<n: #a리스트의 요소들이 남음
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]
for x in c:
    print(c, end=' ')
    
    
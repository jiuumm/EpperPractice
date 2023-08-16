n= int(input())
#가장 자리 0으로 초기화 하는 방법
lst=[list(map(int, input().split())) for _ in range(n)]
lst.insert(0, [0]*n)
lst.append([0]*n)

for x in lst:
    x.insert(0,0)
    x.append(0)
# 오른쪽, 왼쪽, 위쪽, 아래쪽    
dx = [1, -1, 0, 0 ]
dy = [0, 0, -1, 1 ]

cnt=0

for i in range(1, n+1):
    for j in range(1, n+1):
        #모든 조건이 참이 될 때-> all이 참이 된다.
        if all(lst[i][j]>lst[i+dx[k]][j+dy[k]] for k in range(4)): 
            cnt+=1
            
print(cnt)
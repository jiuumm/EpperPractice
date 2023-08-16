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

x = 1
y = 1

res=0   
for i in range(1, n+1):
    for j in range(1, n+1):
        if lst[x+dx[0]][y+dy[0]]<lst[x][y] and lst[x+dx[1]][y+dy[1]]<lst[x][y] and lst[x+dx[2]][y+dy[2]]<lst[x][y] and lst[x+dx[3]][y+dy[3]]<lst[x][y]:
            res+=1
            
        x+=1
        if j==n:
            x=1
            y+=1

'''
+FeedBack
i, j가 행과 열을 나타내는데 굳이 x,y를 쓸 필요가 없었음.
'''         
    


print(res)
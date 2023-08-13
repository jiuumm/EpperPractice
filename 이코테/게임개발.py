n, m= map(int, input().split())
x,y,direction= map(int, input().split())
res=1 #방문한 칸의 수

history = [[0]*m for _i in range(n)] #방문한 위치정보 저장 ->갈 수 있는 곳:0, 이미 가본 곳: 1
history[x][y]=1 #현재 위치한 곳에는 반드시 방문을 했었음.-> 1저장

array=[] #island의 map정보
for i in range(n):
    
    array.append(list(map(int, input().split())))   

#차례대로 북쪽, 서쪽, 남쪽, 동쪽을 바라보고 있을 때 이동할 방향 리스트
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
turnTime =0
def turnLeft(): #왼쪽으로 회전하는 함수
    global direction
    direction-=1
    if direction==-1:
        direction=3

while True:
    turnLeft()
    new_x= x+dx[direction]
    new_y= y+dy[direction]
    
    if history[new_x][new_y]==0 and array[new_x][new_y] == 0: #가야할 위치가 가보지 않았고 육지라면
        history[new_x][new_y]= 1 #그곳으로 가기
        x=new_x #현재 map상에 있는 위치도 갱신
        y=new_y #y위치도 갱신
        res+=1 #가본 곳 +1
        turnTime +=1
        continue #그리고 다시 turnLeft함수 실행
    
    else: #더이상 못간다면?
        turnTime+=1 #회전하기
    
    if turnTime==4: #4번 다 돌았는데도 못간다면 그냥 끝내야함
        new_x = x-dx[direction]
        new_y= y-dy[direction]
        if array[new_x][new_y] ==0: #뒤로 가려는 곳이 육지라면 가도 됨
            x=new_x
            y=new_y
        else: #만약 바다면
            break
        turnTime=0
print(res)
    


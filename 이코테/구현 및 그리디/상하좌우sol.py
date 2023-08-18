n= int(input())
x,y =1,1
plans=  input().split() #plans = [ R R R U D D]

#L, R, U, D
dx = [0,0,-1, 1]
dy = [-1, 1, 0, 0]
move_types =["L", "R", "U", "D"]

for plan in plans:
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx= x+dx[i]
            ny = y+dy[i]
    if nx<1 or nx>n or ny<1 or ny>5:
        continue #지도를 벗어나면 그냥 대입을 안함으로써 무시한다.
    x,y = nx, ny

print(x,y)


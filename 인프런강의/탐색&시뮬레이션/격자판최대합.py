n= int(input())
board=[list(map(int, input().split())) for _ in range(n)]

#행, 열, 대각선 방향
dx = [0,1,1,1]
dy = [1,0,1,-1]

#행들의 합[row]
x=y=0
sum_row=0
for i in range(n):
    sum_row +=board[x][y]
    x= i+dx[0]
    y = y+dy[0]
    
#열들의 합[column]
x=y=0
sum_col=0
for i in range(n):
    sum_col+=board[x][y]
    x = x+dx[1]
    y = i+dy[1]

#대각선들의 합[dia]
sum_dia1 = 0
x=y=0
for i in range(n):
    sum_dia1+=board[x][y]
    x = x + dx[2]
    y = y + dy[2]

sum_dia2 = 0    
x=0
y=n-1
for i in range(n):
    sum_dia2+=board[x][y]
    x = x + dx[3]
    y = y + dy[3]

new=[]
new.append(sum_col)
new.append(sum_row)
new.append(sum_dia1)
new.append(sum_dia2)

new.sort(reverse=True)
print(new[0])


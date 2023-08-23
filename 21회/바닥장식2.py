#재귀함수 부르기
#dfs함수 역할, solution 역할
'''
1. dfs함수 역할
같은 모양이면 그냥 계속 재귀함수부름
이때, 모양에는 ㅡ 모양과 ㅣ 모양이 있는데, 각각의 경우 어떻게 탐색할 지를 정한다.
한 마디로, dfs함수는 탐색하는 함수이다.

2. solution 역할
방문한 곳 check,
만약 방문을 안했다면 방문하기! -> dfs가서 탐색시작

'''
def dfs(board, x, y, n, m, visited):
    nx, ny=0,0
    visited[y][x]=True
    
    if board[y][x]=='ㅡ':
        nx=x+1
        ny=y
    else:
        nx=x
        ny=y+1
    
    if nx<m and ny<n and not visited[nx][ny] and board[x][y]==board[nx][ny]:
        dfs(board, nx,ny, n, m, visited) 




def solution(board, n, m):
    visited = [[False]*(m) for _ in range(n)]
    answer=0
    
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            dfs(board, i, j,n, m, visited)
            answer+=1
    return answer

if __name__=='__main__':
    n, m= map(int, input().split())
    board=[]
    for _ in range(n):
        board.append(list(map(int, input().split())))
        
    print(solution(board, n, m))
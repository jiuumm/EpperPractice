def dfs(board, m, n, x, y, visited ):
    nx, ny = 0, 0
    visited[x][y]=True
    
    if board[x][y]=='ㅡ':
        nx=x
        ny=y+1
    else:
        nx=x+1
        ny=y
        
    if nx<n and ny<m and board[nx][ny]==board[x][y] and not visited[nx][ny]:
        dfs(board, m, n, nx, ny, visited)

    
def solution(board, m, n):
    answer = 0
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            dfs(board, m, n, i, j, visited)
            answer+=1    
    return answer     

if __name__ == '__main__':
    n,m= map(int, input().split())#n, m:행, 열
    board=[]
    for _ in range(n):
        tmp=input()
        board.append(tmp)
    print(solution(board, m, n))

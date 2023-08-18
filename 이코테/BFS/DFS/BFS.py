def dfs(graph, v, visited):
    #v번 노드 접근
    visited[v] = True #방문한 노드 true로 바꾸기
    print(v, end=' ') #방문한 노드 출력
    
    for i in graph[v]:#v번 노드와 연결된 노드들
        if not visited[i]:
            dfs(graph, i, visited)
            
            
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False]*9

dfs(graph,1, visited )
        
def dfs_edges(G, source, depth_limit=None, visited = None): 
    """
    G에서 source로부터 가능한 depth_limit에 대한 traversal
    depth_limit는 source로부터의 거리를 의미한다. 
    depth를 고정하면서 탐색
    ---- 
    visited: 방문한 node들을 업데이트해줌. recursion에서 deep copy되는 것이 아니므로 
    같은 컨테이너가 공유되므로, 다른 함수들에서도 동일하게 visited여부를 체크할 수 있음.
    not_visited_nbrs: 방문하지 않는 source의 neighbor들
    """
    if depth_limit is None: 
        depth_limit = len(G)
    if visited is None: 
        # python의 모든 것은 object이며 function 또한 마찬가지임. 
        # 즉, parameter의 초기 값을 위처럼 정하면, 함수가 처음 콜되었을 때 내부 변수로 정의됨. 
        # 따라서, 만약 다음에 같은 함수를 콜하게 되면 해당 값을 그대로 가져오게 됨. 
        # 따라서, 매번 내부에서 초기화해주는 방식이 좋음.
        visited = set()
        visited.update([source])
    not_visited_nbrs = set(G[source]) - visited
    if len(not_visited_nbrs) > 0:
        # neighbor들을 순차적으로 돌아감.
        for next_source in not_visited_nbrs: 
            if next_source not in visited: 
                # next_source에 방문하지 않았으면 방문하고 edge를 yield하고 업데이트
                yield (source, next_source)
                visited.update([next_source])
                # depth_limit가 2보다 크거나 같으면 다음 recursion 실행.
                if depth_limit >= 2: 
                    yield from dfs_edges(G, next_source, depth_limit=depth_limit-1, visited=visited)
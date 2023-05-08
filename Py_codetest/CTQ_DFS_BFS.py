# 5-9 음료수 얼려 먹기

def solution(_map):
    visited = []
    num_of_ice = 0

    # 각 노드를 순회하면서 DFS를 실행합니다.
    for i in range(len(_map)):
        for j in range(len(_map[i])):
            coord = (i, j)
            if New_dfs(_map, coord, visited):
                num_of_ice += 1

    return num_of_ice


# 단순히 좌표를 계산하는 함수입니다.
def add_coord(c1):
    def _add_coord(c2):
        return c1[0] + c2[0], c1[1] + c2[1]

    return _add_coord


# 해당 좌표가 범위 내인지 확인하는 함수입니다.
def is_in_boundary(_map):
    def _is_in_boundary(c):
        is_in_row = 0 <= c[0] < len(_map)
        if not is_in_row:
            return False
        is_in_column = 0 <= c[1] < len(_map[c[0]])
        if not is_in_column:
            return False
        return True

    return _is_in_boundary


# 해당 좌표가 빈칸인지 확인하는 함수입니다.
def is_empty(_map):
    def _is_empty(c):
        return _map[c[0]][c[1]] == 0

    return _is_empty


# 해당 좌표가 방문하지 않은 노드인지 확인하는 함수입니다.
def is_not_visited(visited):
    def _is_not_visited(c):
        return c not in visited

    return _is_not_visited


# DFS 함수입니다.
def New_dfs(_map, coord, visited):
    # 탈출 조건 (False를 반환하여, 서브 그래프를 구성하지 않는다는 것을 알립니다.)
    if _map[coord[0]][coord[1]] == 1 or coord in visited:
        return False

    # 방문처리
    visited.append(coord)
    path = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    neighbor = list(filter(is_not_visited(visited),
                           filter(is_empty(_map), filter(is_in_boundary(_map), map(add_coord(coord), path)))))

    for n in neighbor:
        New_dfs(_map, n, visited)

    # 루트 노드 하나로 이루어진 서브 그래프의 경우도 고려해야 하므로 여기서 True를 반환힙니다.
    return True


# 5-11 미로 탈출 문제
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의 (상, 하, 좌, 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# bfs 소스코드 구현
def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간 범위를 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

# bfs를 수행한 결과 출력
print(bfs(0,0))














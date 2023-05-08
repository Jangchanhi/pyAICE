# 탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
# 자료구조 : 데이터를 표현하고 관리하고 처리하기 위한 구조
from collections import deque

# 스택 : 선입추훌, 또는 후입 선출 구조
# 5-1 스택 예제 1
# stack = []
#
# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()
# stack.append(1)
# stack.append(4)
# stack.pop()
#
# print(stack)
# print(stack[::-1])

# 5-2 큐 : 선입선출 구조
# queue = deque()
#
# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()
# 
# print(queue) # 먼저 들어온 순서대로 출력
# queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
# print(queue) # 나중에 들어온 원소부터 출력

# 5-6 인접 행렬 방식
# INF =  99999999
# graph = [
#     [0,7,5],
#     [7,0,INF],
#     [5,INF,0]
# ]
# print(graph)
# 
# # 5-7 인접 리스트 방식
# # 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
# graph = [[] for _ in range(3)]
# 
# graph[0].append((1, 7)) # 노드 0에 연결된 노드 정보 저장(노드, 거리)
# graph[0].append((2, 5))
# graph[1].append((0, 7)) # 노드 1에 연결된 노드 정보 저장(노드, 거리)
# graph[2].append((0, 5)) # 노드 2에 연결된 노드 정보 저장(노드, 거리)
# print(graph)

# 5-8 DFS 예제 => 스택 자료구조에 기초한다 (실제는 스텍을 안써도 되며 탐색할 때 데이터가 N개일 경우 O(N)의 시간이 소요된다.
# DFS 특징 : 재귀 함수를 이용할 때 간결하게 구현 가능하다, 최대한 멀리 있는 노드를 우선으로 탐색하는 방식
# 
def dfs(graph, v, visited):
    # 현재노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs_ice(graph, i)
# # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]
# # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
# visited = [False] * 9
# # 정의된 DFS 함수를 호출한다
# dfs(graph, 1, visited)

# BFS : 너비 우선 탐색 => 가까운 노드부터 탐색하는 알고리즘
# # 5-9 BFS 예제
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
# 
# visited = [False] * 9 # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
# bfs(graph, 1, visited) # BFS 함수 호출

# 5-10문제 : 음료수 얼려먹기
# N, M을 공백으로 구분해서 입력 받음
n, m = map(int, input().split())

# 2차원 리스트의 맴 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs_ice(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y > m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs_ice(x - 1, y)
        dfs_ice(x, y - 1)
        dfs_ice(x + 1, y)
        dfs_ice(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs_ice(i, j) == True:
            result += 1

print("아이스크림의 개수는?")
print(result)




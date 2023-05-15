from collections import deque
from itertools import combinations

# # Q15
# # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
# n, m, k, x = map(int, input().split())
# graph = [[] for _ in range(n+1)]
#
# # 모든 도로 정보 입력받기
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#
# # 모든 도시에 대한 차단 거리 초기화
# distance = [-1] * (n+1)
# distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정
#
# q = deque([x])
# while q:
#     now = q.popleft()
#     # 현재 도시에서 이동할 수 있는 모든 도시를 확인
#     for next_node in graph[now]:
#         # 아직 방문 안한 도시
#         if distance[next_node] == -1:
#             distance[next_node] = distance[now] + 1
#             q.append(next_node)
#
# # 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
# check = False
# for i in range(1, n+1):
#     if distance[i] == k:
#         print(i)
#         check = True
#
# # 만약 최단 거리가 K인 도시가 없다면, -1 출력
# if check == False:
#     print(-1)


# # Q16 연구소
# n, m = map(int, input().split())
# data = [] # 초기 멥 리스트
# temp = [[0] * m for _ in range(n)]
# 
# for _ in range(n):
#     data.append(list(map(int, input().split())))
# 
# # 4가지 이동 방향에 대한 리스트
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# 
# result = 0
# 
# # 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
# def virus(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
#         if nx >= 0 and nx < n and ny >= 0 and ny < m:
#             if temp[nx][ny] == 0:
#                 temp[nx][ny] = 2
#                 virus(nx, ny)
# 
# # 현재 맵에서 안전 영역의 크기 계산하는 메서드
# def get_score():
#     score = 0
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j] == 0:
#                 score += 1
#     return score
# 
# # DFS로 울타리 설치하면서, 매번 안전 영역의 크기 계산
# def dfs_virus(count):
#     global result
#     # 울타리가 3개 설치된 경우
#     if count == 3:
#         for i in range(n):
#             for j in range(m):
#                 temp[i][j] = data[i][j]
#         # 각 바이러스의 위치에서 전파 발생
#         for i in range(n):
#             for j in range(m):
#                 if temp[i][j] == 2:
#                     virus(i, j)
#         # 안전 영역의 최대값 계산
#         result = max(result, get_score())
#         return
#     # 빈 공간에 울타리 설치
#     for i in range(n):
#         for j in range(m):
#             if data[i][j] == 0:
#                 data[i][j] = 1
#                 count += 1
#                 dfs_virus(count)
#                 data[i][j] = 0
#                 count -= 1
# 
# dfs_virus(0)
# print(result)

# # Q 17 경쟁적 전염

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 산입
            data.append((graph[i][j], 0, i, j))
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 원칙
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])

# Q 21 인구 이동

# Q 22 블록 이동하기









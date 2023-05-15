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
#
# n, k = map(int, input().split())
#
# graph = [] # 전체 보드 정보를 담는 리스트
# data = [] # 바이러스에 대한 정보를 담는 리스트
#
# for i in range(n):
#     # 보드 정보를 한 줄 단위로 입력
#     graph.append(list(map(int, input().split())))
#     for j in range(n):
#         # 해당 위치에 바이러스가 존재하는 경우
#         if graph[i][j] != 0:
#             # (바이러스 종류, 시간, 위치 X, 위치 Y) 산입
#             data.append((graph[i][j], 0, i, j))
# data.sort()
# q = deque(data)
#
# target_s, target_x, target_y = map(int, input().split())
#
# # 바이러스가 퍼져나갈 수 있는 4가지 원칙
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# # 너비 우선 탐색(BFS) 진행
# while q:
#     virus, s, x, y = q.popleft()
#     # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
#     if s == target_s:
#         break
#     # 현재 노드에서 주변 4가지 위치를 각각 확인
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         # 해당 위치로 이동할 수 있는 경우
#         if 0 <= nx and nx < n and 0 <= ny and ny < n:
#             # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
#             if graph[nx][ny] == 0:
#                 graph[nx][ny] = virus
#                 q.append((virus, s + 1, nx, ny))
#
# print(graph[target_x - 1][target_y - 1])
#

# Q 18 괄호 변화

# Q 19 연산자 끼워 넣기
#
# n = int(input())
# # 연산을 수행하고자 하는 수 리스트
# data = list(map(int, input().split()))
# # 더하기, 빼기, 곱하기, 나누기 연산자 개수
# add, sub, mul, div = map(int, input().split())
#
# # 최솟값과 최댓값 초기화
# min_value = 1e9
# max_value = -1e9
#
# # 깊이 우선 탐색(DFS) 메서드
# def dfs(i, now):
#     global min_value, max_value, add, sub, mul, div
#     # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 엄데이트
#     if i == n:
#         min_value = min(min_value, now)
#         max_value = max(max_value, now)
#     else:
#         # 각 연산자에 대하여 재귀적으로 수행
#         if add > 0:
#             add -= 1
#             dfs(i+1, now + data[i])
#             add += 1
#         if sub > 0:
#             sub -= 1
#             dfs(i + 1, now - data[i])
#             sub += 1
#         if mul > 0:
#             mul -= 1
#             dfs(i + 1, now * data[i])
#             mul += 1
#         if div > 0:
#             div -= 1
#             dfs(i + 1, int(now / data[i])) # 나눌 때는 나머지를 제거
#             div += 1
# # DFS 메서드 호출
# dfs(1, data[0])
# # 최댓값과 최솟값 차례대로 출력
# print(max_value)
# print(min_value)

# Q 20 감시 피하기

n = int(input()) # 복도의 크기
board = [] # 복도 정보(N x N)
teachers = [] # 모든 선생님 위치 정보
spaces = [] # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teachers.append((i, j))
        # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
        if board[i][j] == 'X':
            spaces.append((i,j))

# 특정 방향으로 감시를 진행(학생 발견: True, 학생 미발견: False)
def watch(x, y, direction):
    # 왼쪽 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y -= 1
    # 오른쪽 방향으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    # 위쪽 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    # 아래 방향으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False
# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생님의 위치를 하나씩 확인
    for x, y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True
        return False
    find = False  # 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    # 장애물 설치해보기
    for x, y in data:
        board[x][y] = 'O'
    # 학생이 한 명도 감지되지 않는 경우
    if not process():
        # 원하는 경우를 발견한 것임
        find = True
        break
    # 설치된 장애물을 다시 없대기
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('Yes')
else:
    print('NO')


# Q 21 인구 이동

# Q 22 블록 이동하기









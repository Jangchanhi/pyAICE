# 문제 1상하좌우

# 첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1<= N <=100)
# 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1<= 이동횟수 <=100)
#

# # 방법 1. 채텍
# n = int(input())
# map = list(map(str, input().split()))
# x, y = 1, 1
#
# for m in map:
#     if m == 'R':
#         y = y+1 if y+1 <= n else y
#     if m == 'L':
#         y = y-1 if y-1 >= 1 else y
#     if m == 'U':
#         x = x-1 if x-1 >= 1 else x
#     if m == 'D':
#         x = x+1 if x+1 <= n else x
#
# print(x, y)

# # 문제 1 풀이 방법 no.2
# N을 입력받기
# n = int(input())
# x, y = 1,1
# plans = input().split()
#
# # L, R, U, D [왼, 오, 위, 아래]
# move_x = [0, 0, -1, 1]
# move_y = [-1, 1, 0, 0]
#
# move_type = ['L', 'R', 'U', 'D']
#
# for plan in plans:
#     for i in range(len(move_type)):
#         if plan == move_type[i]:
#             nx = x + move_x[i]
#             ny = y + move_y[i]
#         if nx < 1 or ny < 1 or nx > n or ny > n:
#             continue
#
#     x, y = nx, ny
#
# print(x, y)

# 문제 4-2 시각
# #
time = int(input())

count = 0
for i in range(time+1):
     for j in range(60):
         for k in range(60):
                if i % 10 == 3 or j / 10 == 3 or j % 10 == 3 or k / 10 == 3 or k % 10 == 3 :
                    count += 1

print(count)

# count_h = 0
# count_m = 0
# count_s = 0
#
# for i in range(time+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' == str(i):
#                 count += 1
#             if '3' == str(j):
#                 count += 1
#             if '3' == str(k):
#                 count += 1
#             if '3' == str(i) or '3'== str(j):
#                 count += 1
#             if '3' == str(j) or '3'== str(k):
#                 count += 1
#             if '3' == str(i) or '3'== str(k):
#                 count += 1
#             if '3' == str(i) or '3'== str(j) or '3'== str(k):
#                 count += 1

# 
# for i in range(time+1):
#     for j in range(60):
#         for k in range(60):
#             if str(time) in str(i) + str(j) + str(k):
#                 count += 1






# for i in range (time+1):
#     if str(time) == str(i):
#         count +=1
#         for j in range(60):
#                 if str(time) == str(i) or str(time) == str(j):
#                     count += 1
#                     for k in range(60):
#                             if str(time) == str(i) or str(time) == str(j) or str(time) == str(k):
#                                 count += 1


# for i in range (time+1):
#     if str(time) == str(i):
#         count_h += 1
#         count += count_h
#     for j in range(60):
#         if str(time) == str(j):
#             count_m = count + 1
#             count += count_m
#         for k in range(60):
#             if str(time) == str(k):
#                 count_s = count + 1
#                 count += count_s
# 
# print(count)

# 왕실 나이트
# 
# N = list(input())
# location = [0, 0]
# answer = 0
# x = ['1', '2', '3', '4', '5', '6', '7', '8']
# y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# 
# # 행렬로 변환
# for i in range(8):
#     if N[1] == x[i]:
#         location[0] = i
#     if N[0] == y[i]:
#         location[1] = i
# 
# # 나이트가 움직일수 있는 8가지 타입을 인덱스별로 만듬
# dx = [-2, -2, 2, 2, -1, 1, -1, 1]
# dy = [-1, 1, -1, 1, -2, -2, 2, 2]
# 
# # 타입별로 돌아봤을 때 매트릭스 안에서 움직일 수 있다면 answer += 1
# for i in range(8):
#     if location[0] - dx[i] >= 0 and location[1] - dy[i] >= 0 and location[0] - dx[i] <= 7 and location[1] - dy[i] <= 7:
#         answer += 1
#     else:
#         continue
# 
# print(answer)


# import sys
#
# # 현재 나이트가 위치한 곳의 좌표 입력받기
# location = sys.stdin.readline().rstrip()
# x = ord(location[0]) - 96
# y = int(location[1])
#
# # 나이트가 움직일 수 있는 최대 경우의 수는 8가지
# answer = 8
#
# # 1. 1번으로 나이트가 못 움직이는 경우
# if y == 1 or y == 2 or y == 7 or y == 8:
#   # 1-1. 한쪽 수직으로 두 칸 이동할 수 없는 경우
#   answer -= 2
#   if x == 1 or x == 8:
#     # 1-2. 한쪽 수직으로 두 칸 이동할 수 없으면서 수평으로 한 칸 이동할 수 없는 경우
#     answer -= 1
# else:
#   # 1-3. 양쪽 수직으로 두 칸 이동할 수 있지만 수평으로 한 칸 이동할 수 없는 경우
#   if x == 1 or x == 8:
#     answer -= 2
#
# # 2. 2번으로 나이트가 못 움직이는 경우
# if x == 1 or x == 2 or x == 7 or x == 8:
#   # 2-1. 한쪽 수평으로 두 칸 이동할 수 없는 경우
#   answer -= 2
#   if y == 1 or y == 8:
#     # 2-2. 한쪽 수평으로 두 칸 이동할 수 없으면서 수직으로 한 칸 이동할 수 없는 경우
#     answer -= 1
# else:
#   # 2-3. 양쪽 수평으로 두 칸 이동할 수 있지만 수직으로 한 칸 이동할 수 없는 경우
#   if y == 1 or y == 8:
#     answer -= 2
#
# print(answer)

# 구현 실전문제 <3> 게임 개발
# # N, M을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())
#
# # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
# d = [[0]*m for _ in range(n)]
#
# x, y, direction = map(int, input().split())
# d[x][y] = 1 # 현재 좌표 방문 처리
#
# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3
#
# # 시뮬레이션 시작
# count = 1
# turn_time = 0
# while True:
#     # 왼쪽
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#
#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] = 1
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue
#     # 회전한 이후에 정면에 못가본 칸이 없거나 바다일 경우
#     else:
#         turn_time += 1
#
#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#
#         # 뒤로 수 있으면 이동
#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
#         # 뒤가 바다로 막혀있을 경우
#         else:
#             break
#         turn_time = 0
#
# print(count)













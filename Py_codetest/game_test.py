# n, m = map(int, input().split())
# x, y, h = map(int, input().split())
#
# map1 = []
# for i in range(n):
#     map1.append(list(map(int, input().split())))
#
# isavail = [(-1, 0), (0,1), (1,0), (0,-1)]
# map1[x][y] = 1
# count = 0
# result = 1
#
# while True:
#     if h == 0 :
#         h = 3
#     else :
#         h -= 1
#
#     nx = x + isavail[h][0]
#     ny = y + isavail[h][1]
#
#     if nx < 0 or nx >= n or ny < 0 or ny >= m or map1[nx][ny] == 1:
#         count += 1
#         if count == 5: #만약 5번이상 이동없이 회전한다면 더이상 이동할 곳이 없다는 뜻이므로 반복문 탈출
#             break
#         continue
#
#     x = nx
#     y = ny
#     map1[x][y] = 1
#     result += 1
#     count = 0
#
# print(result)

#
#
# n = int(input())
# way = input().split()
#
# location = [1, 1]
#
# L = [-1, 0]
# R = [1, 0]
# U = [0, 1]
# D = [0, -1]
#
#
# for i in way:
#     match i:
#         case 'L':
#             if location[0] <= 1:
#                 continue
#             else:
#                 location = [x + y for x, y in zip(location,L)]
#         case 'R':
#             if location[0] >= n:
#                 continue
#             else:
#                 location = [x + y for x, y in zip(location,R)]
#         case 'U':
#             if location[1] <= 1:
#                 continue
#             else:
#                 location = [x + y for x, y in zip(location,U)]
#         case 'D':
#             if location[1] >= n:
#                 continue
#             else:
#                 location = [x + y for x, y in zip(location,D)]
#
# print(location[0], location[1])
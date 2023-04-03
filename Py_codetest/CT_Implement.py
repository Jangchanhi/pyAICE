# 상하좌우 

# 첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1<= N <=100)
# 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1<= 이동횟수 <=100)
#

n = int(input())
map = list(map(str, input().upper().split()))
x, y = 1, 1

for m in map:
    if m == 'R':
        y = y+1 if y+1 <= n else y
    if m == 'L':
        y = y-1 if y-1 >= n else y
    if m == 'U':
        y = x-1 if x-1 >= n else x
    if m == 'D':
        y = x+1 if x+1 <= n else x

print(x, y)
# # N을 입력받기
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














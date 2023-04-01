# 모험가 길드 문제
#
# print("모험가 수 입력")
#
# n = int(input())
# man = list(map(int, input().split()))
# man.sort()
#
# count = sum = 0
# for t in man:
#     sum += 1
#     if sum == t:
#         count += 1
#         sum = 0
#
# print(count)

# # 곱하기 혹은 더하기
# print("문자열을 입력하시오(숫자만)")
# num = input()
# answer = int(num[0])
#
# for i in range(1, len(num)):
#     if answer < 1 or int(num[i]) < 1:
#         answer = answer + int(num[i])
#     else :
#         answer = answer * int(num[i])
#
# print(answer)
#
# for i in range(1, len(num)):
#     if int(num[i]) < 1 or answer < 1:
#         answer = answer + int(num[i])
#     else :
#         answer = answer * int(num[i])

# # <안됨>
# for i in range(1, len(num)):
#     if int(num[i]) >= 1 or answer >= 1:
#         answer = answer * int(num[i])
#     else :
#         answer = answer + int(num[i])

# 문자열 뒤집기 문제
#
# print("문자열을 입력하시오(ex. 01010101)")
# S = input()
#
# count0 = len(list(filter(lambda x: len(x) > 0, S.split('0'))))
# count1 = len(list(filter(lambda x: len(x) > 0, S.split('1'))))
#
# print(min(count0, count1))


# # 동전 갯수 입력
# n = int(input())
#
# # 화폐 단위 입력
# coin_list = list(map(int, input().split()))
#
# # 화폐를 크기가 작은 순부터 오름차순 정렬
# coin_list.sort()
#
# ### 정답 해설 방법 ###
#
# target = 1 # 해당 변수에 화폐를 작은 순 부터 더해 해당 값이 다음 화폐보다 작으면 만들 수 없는 값이 된다.
# for x in coin_list:
#     # 만들 수 없는 금액을 찾았을 때 반복 종료
#     if target < x:
#         break
#     target += x
#
# # 만들 수 없는 금액 출력
# print(target)
#
# from itertools import combinations
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# bowling_balls = list(map(int, input().split()))
# count = 0
#
# for combi in combinations([i for i in range(1, n+1)], 2):
#     if bowling_balls[combi[0]-1] != bowling_balls[combi[1]-1]:
#         count += 1
#
# print(count)
#
# # 04 만들 수 없는 금액 heapq한 방법
# import time
# import heapq
#
# s_time = time.time()
#
# coin_n = int(input())
# coin_unit = list(map(int, input().split()))
# heapq.heapify(coin_unit)
#
# result = 1
#
# while coin_unit:
#     num = heapq.heappop(coin_unit)
#     if result < num:
#         break
#     result = result + num
#
# print(result)
#
# end_t = time.time()
# print("프로그램 수행 시간은?", end_t - s_time)

#
# from collections import deque
#
# print("볼링공의 개수와 무게는?")
# n, m=map(int, input().split())
# s=list(map(int, input().split()))
#
#
# q=deque(s)
# count=0
# while q :
#     temp=q.popleft()
#     for i in q :
#         if i!=temp :
#             count+=1
#
# print(count)


#
# import heapq
#
# def solution(food_times, k):
#     # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
#     if sum(food_times) <= k:
#         return -1
#
#     # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
#     q = []
#     for i in range(len(food_times)):
#         # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
#         heapq.heappush(q, (food_times[i], i + 1))
#
#     sum_value = 0 # 먹기 위해 사용한 시간
#     previous = 0 # 직전에 다 먹은 음식 시간
#     length = len(food_times) # 남은 음식의 개수
#
#     # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
#     while sum_value + ((q[0][0] - previous) * length) <= k:
#         now = heapq.heappop(q)[0]
#         sum_value += (now - previous) * length
#         length -= 1 # 다 먹은 음식 제외
#         previous = now # 이전 음식 시간 재설정
#
#     # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
#     result = sorted(q, key=lambda x: x[1]) # 음식의 번호 기준으로 정렬
#     return result[(k - sum_value) % length][1]
#
#
# print("문자열을 입력하시오(ex. 01010101)")
# S = input()
#
# count0 = len(list(filter(lambda x: len(x) > 0, S.split('0'))))
# count1 = len(list(filter(lambda x: len(x) > 0, S.split('1'))))
#
# print(min(count0, count1))






# 그리디 알고리즘
# 3-1 거스름돈 문제
#
# money = 0 # 입력한 돈
# count = 0 # 동전의 개수
# coins = [500, 100, 50, 10]
#
# print("점원에게 줄 돈은 얼마인가요?")
# money = int(input("돈 : "))
# print(money)
#
# for coin in coins:
#     count += money // coin # // : 몫을 구하는 연산자
#     money %= coin # #: 나머지를 구하는 연산자
#
# print("동전의 개수")
# print(count)

# 3-2 큰 수의 법칙
# n : 배열의 크기, m : 숫자 더하는 횟수, k : 최대 값이 연속할 수 있느 횟수


# 방법 1
# first = d_list[n-1] # 가장 큰 수
# second = d_list[n-2] # 두 번째로 큰 수
#
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1

# # 방법 2
# n, m, k = map(int, input().split()) # 자연수 : int 사용
# result = 0
# #
# d_list = list(map(int, input().split()))
# d_list.sort() # 입력한 수를 정렬
#
# count = (m//(k+1))*k
# count += m % (k+1)
# result = 0
# result += count * d_list[n-1] # 가장 큰 수 더하기
# result += (m-count) * d_list[n-2] # 두 번째 큰 수 더하기
#
# print("결과 값")
# print(result)

# 3-3 숫자 카드 게임
# # n : 행의 개수, m : 열의 개수
# n, m = map(int, input().split())
# result = 0
# # 첫번 째 1행 부터 시작
# for i in range(n):
#     d = list(map(int, input().split()))
#     # 현재 행에서 가장 작은 수를 찾는다.
#
#     min_v = 10000
#     # 가장 작은 수들 중에서 제일 큰 수를 찾는다.
#     for j in d:
#         min_v = min(min_v, j)
#
#     result = max(result, min_v)
#
# print(result)

# 3-4 1이 될 때까지
n, k = map(int, input().split())
result = 0
# n이 k 보다 크다면 k로 계속 나눠야 한다.
# 1. n이 k로 나눠지지 않으면 1 빼기
# 2. k로 나눠지면 나누기
# 3. 남은 수에 대해 1씩 계속 빼기
while n >=k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1
print(result)








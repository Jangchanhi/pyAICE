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

print("문자열을 입력하시오(ex. 01010101)")
S = input()

count0 = len(list(filter(lambda x: len(x) > 0, S.split('0'))))
count1 = len(list(filter(lambda x: len(x) > 0, S.split('1'))))

print(min(count0, count1))














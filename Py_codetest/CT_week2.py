# A01 모험가 길드 문제
#
# print("모험가의 수는?")
# n = int(input())
#
#
#
# data = list(map(int, input().split()))
# data.sort()
#
# result = 0
#
# # 현재 그룹에서의 모험가 수
# count = 0
#
# for i in data:
#     count = count + 1
#     if count >= i:
#         result += 1
#         count = 0
#
# print("총 그룹의 수는 ?")
# print(result)

print(" A 02 곱하기 혹은 더하기 문제")

data = input()

result = int(data[0])

for i in range(1, len(data)):

    num = int(data[i])
    if num <= 1 or result  <= 1:
        result += num
    else:
        result *= num
print(result)



# A01 모험가 길드 문제
#
# print("모험가의 수는?")
# n = int(input())
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
#
# print(" A 02 곱하기 혹은 더하기 문제")
#
# data = input()
#
# result = int(data[0])
#
# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
# print(result)

print("A03 문자열 뒤집기")

data = input()

count0 = 0
count1 = 1

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 +=1
print(min(count0, count1))

# A04 문제 만들 수 없는 금액










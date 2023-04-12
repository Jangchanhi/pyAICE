# 07 럭키 스트레이트
#
# print("입력하세요")
# n = input()
# n_lengh = len(n)
# summary = 0
#
# # 왼쪽 부분의 자릿수 합 더하기
# for i in range(n_lengh//2):
#     summary += int(n[i])
#
# # 오른쪽 부분의 자릿수 합 더하기:
# for i in range(n_lengh//2, n_lengh):
#     summary -= int(n[i])
#
# if summary == 0:
#     print('LUCKY')
# else :
#     print("READY")

# # 다른 방법 2
# n_array = list(map(int, input()))
# a = 0 # 앞의 줄
# b = 0 # 뒤의 줄
#
# for i in range(len(n_array)):
#     n = len(n_array) / 2
#     if i < n:
#         a += n_array[i]
#     else:
#         b += n_array[i]
# if a == b:
#     print("Lucky")
# else:
#     print("Ready")


# 08 문자열 재정렬
#
# data = input()
# result = []
# value = 0
#
#
# # 문자를 하나씩 학인
# for x in data:
#     if x.isalpha():
#         result.append()
#     else:
#         value += int(x)
#
# result.sort()
#
# if value != 0 :
#     result.append(str(value))
#
# print(''.join(result))
#
# # 09 문자열 압축
#
# def solution(s):
#     result = []
#     if len(s) ==1:
#         return 1
#
#     for i in range(1, len(s+1)):
#         b = ''
#         count = 1
#         tmp= s[:i]
#
#         for j in range(i, len(s)+i, i):
#
#             if tmp==s[j:i+1]:
#                 count+=1
#             else:
#                 if count!=1:
#                     b = b+str(count)+tmp
#                 else:
#                     b = b + tmp
#
#                 tmp = s[j: j+1]
#                 count = 1
#         result.append(len(b))
#
#     return min(result)

# 문제 12 기동과 보 설치




















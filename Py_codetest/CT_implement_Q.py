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

# # 다른 방법 3
# n_array = input()
# n_half = len(n_array)//2
# right_n = sum([int(num) for num in n_array[:n_half]])
# left_n = sum([int(num) for num in n_array[n_half:]])
#
# if right_n == left_n:
#     print("lucky")
# else :
#     print("ready")

# 08 문자열 재정렬
s = input()

str_array = []
int_array = 0

for i in range(len(s)):
    if s[i] >= 'A' and s[i] <= 'Z':
        str_array.append(s[i])
    elif s[i] >= '0' and s[i] <= '9':
        int_array += int(s[i])

str_array.sort()

print(*str_array, sep='', end='')
# *-> asterisk : for루프 안돌려도 바로 처리가능, 배열 앞에 *연산자 붙여서 함수 호출하면 됨
print(int_array)



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
# # 8번 문제 다른 풀이
# word = input()
# n_list = ['0','1','2','3','4','5','6','7','8','9']
#
# def answer(word, n_list):
#     num = []
#     # 숫자부터 sort로 오름차순으로 정렬
#     word = sorted(word)
#     while True:
#         if word[0] in n_list:
#             num.append(word.pop(0))
#         else:
#             break
#     # 숫자함 구해놓기
#     num = str(sum(list(map(int, num))))
#     # 문자함 구하기
#     st = ''
#     for i in range(len(word)):
#         str += word[i]
#
#     answer = st + num
#     return answer
#
# print(answer(word, n_list))


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




















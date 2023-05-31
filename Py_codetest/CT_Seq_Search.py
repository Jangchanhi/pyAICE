# 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법

# 7-1 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)
# print("생성할 원소 개수를 입력한 다음 한 칸 띄고 ")
# input_data = input().split()
# n = int(input_data[0]) # 원소의 개수
# target = input_data[1] # 찾고자 하는 문자열
#
# print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
# array = input().split()
#
# # 순차 탐색 수행 결과 출력
# print(sequential_search(n, target, array))

# 7-2 재귀 함수로 구현한 이진 탐색 소스코드
def binary_search_J(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 변환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾는 값이 작을 때 왼쪽 확인
    elif array[mid] > target:
        return binary_search_J(array, target, start, mid - 1)
    else:
        return binary_search_J(array, target, mid + 1, end)

#
# n, target = list(map(int, input().split()))
#
# array = list(map(int, input().split()))
#
# result = binary_search_J(array, target, 0, n - 1)
# if result == None:
#     print("원소가 존재하지 않습니다.")
# else:
#     print(result + 1)


# 7-3 반복문으로 구현한 이진 탐색 소스코드
# 이진 탐색 소스코드 구현(반복분)
def binary_search_b(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 때 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# # n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
# n, target = list(map(int, input().split()))
# # 전체 원소 입력받기
# array = list(map(int, input().split()))
#
# # 이진 탐색 수행 결과 출력
# result = binary_search_b(array, target, 0, n - 1)
# if result == None:
#     print("원소가 존재하지 않습니다.")
# else:
#     print(result+1)

# 7-5 실전 문제 2 부품 찾기
def binary_search_n(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# # N(가게의 부품 개수) 입력
# n = int(input())
# # 가게에 있는 전체 부품 번호를 공배긍로 구분하여 입력
# array = list(map(int, input().split()))
# array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행
# # M (손님이 확인 요청한 후 부품개수)입력
# m = int(input()) # 손님이 확인 요청한 전체 부품를 공백으로 구분하고 입력
# x = list(map(int, input().split()))
#
# #  손님이 확인 요청한 부품 번호를 하나식 확인
# for i in x:
#     result = binary_search_n(array, i, 0, n-1)
#     if result != None:
#         print('yes', end=' ')
#     else :
#         print('no', end=' ')

# 7-6 답안 2번째 ( 계수 정렬)
# N 가게의 부품 개수를 입력 받기
n = int(input)
array = [0] * 1000000

for i in input().split():
    array[int(i)] = 1
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 7-7 set() 함수

# N(가게 부품 개수)을 입력받기
n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))
# M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')











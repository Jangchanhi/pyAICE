# 정렬 : 데이터를 특정한 기준에 따라서 순서대로 나열하는 것
# 선택 정렬 : 매번 가장 작은 것을 선택
# 1. 무작위 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 교체,
# 2. 그 후 작은 데이터를 선택해 앞에서 두번 째 데이터와 바꾸는 이 과정을 반복


# # 6-1 선택 정렬 소스 코드
# n = map(int, input().split())
#
# array = []
# for a in range(n):
#     array.append(list(map(int, input())))

array = [7,5,9,0,2,3,5,1,6,8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)













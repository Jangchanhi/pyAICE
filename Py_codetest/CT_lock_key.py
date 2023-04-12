# 10 자물쇠와 열쇠
# 2차원 리스트를 90도 회전하는 함수
def rotate_matrix_by_90degree(a):
    y = len(a) # 행
    x = len(a[0]) # 열
    # 90도로 회전한 후 결과값 다음 2차원 리스트(행, 열 Transpose)
    result = [[0]* y for _ in range(x)]
    for i in range(y):
        for j in range(x):
            result[j][y-i-1] = a[i][j] # y : 행의 개수
    return  result

def check(new_lock):
    origin_lock_len = len(new_lock) // 3
    for i in range(origin_lock_len, origin_lock_len*2):
        for j in range(origin_lock_len, origin_lock_len*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    y = len(lock)
    x = len(key)
    # 자물쇠 길이를 3배로 늘리기
    new_lock = [[0]*(y*3) for _ in range(y*3)]
    # 늘린 자물쇠에 원래 자물쇠 값 갱신
    for i in range(y):
        for j in range(x):
            new_lock[i+y][j+y] = lock[i][j] # 이때, y : 원래 자물쇠 길이

    for _ in range(4):
        key = rotate_matrix_by_90degree(key) # 열쇠 90도 회전
        #회전시킨 열쇠를 자물쇠의 중앙부분에 합치기
        for a in range(y*2):
            for b in range(y*2):
                # 열쇠 끼우기
                for i in range(x):
                    for j in range(x):
                        new_lock[a+i][b+j] += key[i][j]

                # 열쇠 틀(돌기)랑 자물쇠 흠이 맞는지 체크
                if check(new_lock):
                    return True

                # 안맞는 열쇠는 다시 빼기
                for i in range(x):
                    for j in range(x):
                        new_lock[a+i][b+j] -= key[i][j]

    return False

# 기둥과 보 설치 문제

# 해당 x,y 축 기둥이 설치 가능한지 확인
def possible_colum(colum_bo, x, y):
    # 바닥에 붙어있거나, 밑에 기둥이 있거나, 양 끝에 보가 있을 때
    if (y==0) or ([x,y-1,0] in colum_bo) or ([x-1, y,1] in colum_bo) or ([x,y,1] in colum_bo):
        return True
    return False

# 해당 x,y 축 보가 설치 가능한지 확인
def possible_bo(colum_bo, x, y):
    # 양 옆 끝에 기둥이 있거나, 양 옆 보두 보가 있을 때
    if ([x, y-1, 0] in colum_bo) or ([x+1, y-1] in colum_bo) or ([x-1, y,1] in colum_bo and [x+1, y, 1] in colum_bo):
        return True
    return False

def solution(n, build_frame):
    answer = []
    # 설치 되어 있는 기둥과 보
    colum_bo = []

    for build in build_frame:
        x,y,colum_or_bo, del_or_input = build
            # 설치
        if del_or_input ==1:
            # 기둥일 때
            if colum_or_bo ==0:
                # 설치 가능이고 기둥이라면 설치한다.
                if possible_colum(colum_bo, x, y) ==True:
                    colum_bo.append([x,y,colum_or_bo])
            # 보일 때
            else:
                # 설치 가능이고 보면 설치한다.
                if possible_bo(colum_bo, x, y) ==True:
                    colum_bo.append([x,y,colum_or_bo])
        # 삭제
        else:
                # 삭제할 것 임시로 저장해둠
            tmp_save = [x,y,colum_or_bo]
            # 먼저 삭제해버린다.
            colum_bo.remove([x,y,colum_or_bo])
            remove_ok = True
                # 현재 설치된 기둥과 보를 찾고, 설치 불가능이면 삭제 못한다.
            for c_b in colum_bo:
                # 삭제할 것과 x, y축이상 차이나면, 삭제여부에 영향이 없어 넘긴다.
                if abs(tmp_save[0] - c_b[0]) >=2 or abs(tmp_save[1] - c_b[1]) >=2:
                    continue # 기둥이고 해당 기둥에 설치 못하면 삭제 X
                if c_b[2] == 0 and possible_colum(colum_bo, c_b[0], c_b[1]) == False:
                    remove_ok = False
                    break
                # 보일 때고 해당 보에 설치 못하면 삭제 x
                elif c_b[2] == 1 and possible_bo(colum_bo, c_b[0], c_b[1]) == False:
                    remove_ok = False
                    break
            # 삭제할려는데 안되면 삭제 했던 걸 다시 넣어준다.
            if remove_ok == False:
                colum_bo.append(tmp_save)
    return  sorted(colum_bo)






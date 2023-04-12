# 기둥과 보 설치 문제
def possible_colum(colum_bo, x, y):
    if (y==0) or ([x,y-1,0] in colum_bo) or ([x-1, y,1] in colum_bo) or ([x,y,1] in colum_bo):
        return True
    return False

def possible_bo(colum_bo, x, y):
    if ([x, y-1, 0] in colum_bo) or ([x+1, y-1] in colum_bo) or ([x-1, y,1] in colum_bo and [x+1, y, 1] in colum_bo):
        return True
    return False

def solution(n, build_frame):
    answer = []
    colum_bo = []

    for build in build_frame:
        x,y,colum_or_bo, del_or_input = build

        if del_or_input ==1:
            if colum_or_bo ==0:
                if possible_colum(colum_bo, x, y) ==True:
                    colum_bo.append([x,y,colum_or_bo])
            else:
                if possible_bo(colum_bo, x, y) ==True:
                    colum_bo.append([x,y,colum_or_bo])
        else:
            tmp_save = [x,y,colum_or_bo]
            colum_bo.remove([x,y,colum_or_bo])
            remove_ok = True

            for c_b in colum_bo:
                if abs(tmp_save[0] - c_b[0]) >=2 or abs(tmp_save[1] - c_b[1]) >=2:
                    continue # 기둥이고 해당 기둥에 설치 못하면 삭제 X
                if c_b[2] == 0 and possible_colum(colum_bo, c_b[0], c_b[1]) == False:
                    remove_ok = False
                    break
                elif c_b[2] == 1 and possible_bo(colum_bo, c_b[0], c_b[1]) == False:
                    remove_ok = False
                    break
            if remove_ok == False:
                colum_bo.append(tmp_save)


    return  sorted(colum_bo)






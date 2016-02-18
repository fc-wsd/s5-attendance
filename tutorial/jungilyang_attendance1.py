# 수강생 : 양정일 (jungilyang)
# 출석부 만들기1 (Class사용하지 않고)

# 일단 팀원만..
students = '양정일', '신호철', '서자영', '한정현'
attendances = []

# 예외 처리 머시기 아무것도 없습니다. T_T
# time은 YYYYMMDDHHMM
def attend(name, time):
    if name in students :
        attendances.append([name,time])
    else:
        return

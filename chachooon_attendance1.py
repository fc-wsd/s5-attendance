#출석부만들기1
from datetime import datetime

#학생명단
students = ['김용민', '김종록', '박준영', '박한성', '백성훈', '서인용', '서자랑', '손형우', '신승호',
'신호철', '양정길', '윤영식','이승현', '이효준', '장한별', '조혜연', '차정윤', '최현덕', '한정현']

#출석자명단
attendances=[]

#출석처리함수
def attend(student):
    time = datetime.now()
    attendance = [student, time] #출석자 = [이름, 시간]
    if student in students:
        if student in attendences:
            print('이미 출첵 하셨어요.')
        else:
            attendances.append(attendance)
            print('어서오세요.')
            return attendances
    else:
        print('누구세요?')
    print("출석자명단\n" +attendances)

#출석체크
student = input('체크인 하려면 이름을 입력해주세요.\n')
attend(student)

#맞게한건지 되는건지 모르겠어요.

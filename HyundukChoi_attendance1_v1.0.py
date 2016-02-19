# 출석부 만들기 1
from datetime import datetime
date = datetime.now().date().isoformat()

# 학생 명단
students = [
    'hyunduk choi',
    'jeongyoon cha',
    'inyong suh',
    'seungho shin',
    'jonglok kim',
    'yongmin kim',
    'hyojoon lee',
    'junghyun han',
    'seunghyun lee',
    'jungil yang',
    'jarang seo',
    'hanbyul jang',
    'eunsang lee']

# 출석자 명단
attendances = dict()

# 출석 처리 메서드
def attend(student):
    if student in students:
        attendances[student] = date
    else:
        print('student not found. please try again.')

# 모든 학생에 대해서 출석 처리
for student in students:
    attend(student)

# 출석자 명단 출력
print(attendances)

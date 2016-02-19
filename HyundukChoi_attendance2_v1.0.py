# 출석부 만들기 2
from datetime import datetime

# 리스트형 객체 학생 명단
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

# 학생 클래스 생성
class Student():
    def __init__(self, name):
        self.name = name

# 출석부 클래스 생성
class Attendance():
    attendances = dict() # 출석부는 사전형 객체로 생성

    # 출석 처리 메서드
    def attend(self, name):
        date = datetime.now().date().isoformat()
        if name in students:
             self.attendances[name] = date
        else:
            print('student name not found. please try again.')
        return

    # 출석부 출력 메서드
    def list(self):
        return print(self.attendances)

# 예제 코드
att = Attendance()

coi = Student('hyunduk choi')
att.attend(coi.name)
att.list()
print('-'*50)

cha = Student('jeongyoon cha')
att.attend(cha.name)
att.list()
print('-'*50)

suh = Student('inyong suh')
att.attend(suh.name)
att.list()

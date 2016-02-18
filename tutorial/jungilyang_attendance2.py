# 수강생 : 양정일 (jungilyang)
# 출석부 만들기2 (Class사용)

# 일단 팀원만..
students = '양정일', '신호철', '서자영', '한정현'

#Student, Attendance  Class 생성
class Student():
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name

class Attendance():
    def __init__(self):
        self.students_list = []
    def attend(self, Student):
        self.students_list.append(Student.get_name())
    def list(self):
        for name in self.students_list:
            print(name)


## 학생 출석
a = Attendance()
for name in students:
    s = Student(name)
    a.attend(s)
## 출력
a.list()

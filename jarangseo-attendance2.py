#학생명단이 있는 list형 객체 students
students = ['jarangseo','hochulshin','junghyunhan']

class Student():
    name = "name"
    print(name)
    def __init__(self,name):
        self.name = name
    #필수요소 : 이름

#출석부는 Attendance클래스로 생성한 객체
class Attendance():
    attendentList = []
    #attend()인스턴스 메서드로 출석 처리
    #인자는 Student클래스로 만든 학생객체
    @classmethod
    def attend(self,student):
        Attendance.attendentList.append(student)
    #list()인스턴스 메서드로 출석자 명단 출력
    @classmethod
    def printList(self):
        print(Attendance.attendentList)

attendance1 = Attendance()

for name in students:
    studentClass = Student(name)
    attendance1.attend(studentClass.name)
    print(studentClass.name)

attendance1.printList()
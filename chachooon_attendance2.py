#출석부만들기2

students = ['a', 'b', 'c'] #학생명단
attendances =['d'] #출석자명단

class Student(object):
    def __init__(self, name):
        #if name in students:
        self.name = name

class Attendance(Student):
    def attend(self):
        #if self.name not in attendances:
        attendances.append(self.name)
    def list(self):
        return attendances

#출석체크
check = Attendance('a')
print(check.list())

# ... 좌절...왜 안돼는 거죠 

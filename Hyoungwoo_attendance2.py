class Student:
    def stu_list(self, *args):
        self.students=[]
        for arg in args:
            self.students.append(arg)

attendances = []
class Attendance:
    def attend(self, att):
        if att not in stu.students:
            print('There isn\'t \"{}\" in the class.'.format(att))
        else:
            attendances.append(att)
    def list(self):
        return attendances

stu = Student()
stu.stu_list('Son', 'Kay', 'Lee', 'Cha', 'Kim', 'Chang', 'Kim', 'Gang',
            'Shin', 'Park', 'Seo', 'Cho', 'Choi', 'Youn')

att_list = Attendance()
att_list.attend('Son')
att_list.attend('Kay')
att_list.attend('Kim')

print(att_list.list())

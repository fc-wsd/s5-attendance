students = ['jeongyoon cha', 'sancho suh', 'hyunduk choi', 'seungho shin', 'jonglok kim', 'yongmin kim',
    'hyojoon lee', 'hanjunghyun', 'seunghyun lee', 'jungil yang', 'jarang seo'
]

class Student(object) :
    name =""

    def __init__(self, name) :
        self.name = name

    def studentValidation(self) :
        for l_name in students :
            if l_name == self.name :
                return True  # Return True if the name is in the student list
        print("log(studentsValidation) : %s" % self.name )
        print(" is not in the student list")
        return False # else, return False


class Attendance(object) :
    aList = {}

    def attend(self, student, attended_at) :
        if student.studentValidation() :
            self.aList[student.name] = attended_at
            print("log(attend) : succeed in adding attendance to the dictionary")
        else :
            print("log(attend) : %d" % student.name)
            print(" is not in the student list")
    def list(self) :
        print("Num of attendees : %d" % len(self.aList))
        print(self.aList)

att = Attendance()
cha = Student('jeongyoon cha')
suh = Student('sancho suh')

att.attend(cha, '2016-02-18')
att.list()
att.attend(suh, '2016-02-18')
att.list()

#학생명단이 있는 list형 객체 students
students = ['jarangseo','hochulshin','junghyunhan']

#출석자명단 attendances
attendances = []

#attend()함수로 출석처리
def attend(name):
    attendances.append(name)

for name in students:
    attend(students[0])



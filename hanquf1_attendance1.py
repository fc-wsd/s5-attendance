from datetime import datetime

def attend(attendNumber):
    now = datetime.now().date().isoformat() +' ' + datetime.now().time().strftime("%H:%M:%S")
    attendInfo = {"출석시간": now, "이름": students[int(attendNumber)-1]}
    attendances.append(attendInfo)


attendances = []

students = ['김용민', '김종록', '박준영', '박한성', '백성훈',
 '서인용', '서자랑', '손형우', '신승호', '신호철', '양정길', '윤영식',
 '이승현', '이효준', '장한별', '조혜연', '차정윤', '최현덕', '한정현']


while(True):

    print('='*30 )
    print('1. 학생 명단 출력')
    print('2. 출석')
    print('3. 출석한 학생 명단')

    val = input('사용할 기능을 선택해주세요: ')

    if int(val) is 1:
        print('='*10,'학생 명단', '='*10)
        for student in students:
            print(student)
        print('='*30)

    elif int(val) is 2:
        print('='*10,'학생 명단', '='*10)
        num = 1
        for student in students:
            print(num, ':', student)
            num = num + 1

        while(True):
            attendNumber = input('출석 번호를 입력해주세요(끝내려면 0): ')
            if int(attendNumber) is 0:
                break
            attend(attendNumber)
            print(students[int(attendNumber)-1], '출석 완료')

    elif int(val) is 3:
        print('='*10,'출석한 학생 명단', '='*10)
        for attendStudent in attendances:
            print(attendStudent)
    else:
        print(val)
        print('END')
        break




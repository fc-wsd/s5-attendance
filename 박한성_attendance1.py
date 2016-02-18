from datetime import datetime

# 학생 명단
students = ["박한성", "김상범", "서인용", "차정윤", "신호철" ]

# 수강생 정보
attendences = {}

# 날짜 포맷
now = datetime.now()
stamp = now.strftime('%Y-%m-%d')

# 출석 처리 함수
def attend():
	student = input("출석자 이름: ")
	if student in students:
		attendences[student] = stamp
		print (("이름: "), student, ("| 출석일시: "), attendences.get(student))
	else:
		print ("이름을 찾을 수 없습니다. 다시 입력해주세요.")

from datetime import datetime

# 날짜 포맷
now = datetime.now()
stamp = now.strftime('%Y-%m-%d')

# 학생 명단
students = ["박한성", "서인용", "신호철", "차정윤"]

# 출결 클래스
class Student(object):
	def __init__(self, name):
		self.name = name

class Attendance(object):
	attendance = {}
	def attend(self, name):
		if name in students:
			self.attendance[name] = stamp
			print (" %s님 출석되었습니다. | 출석일자: %s " % (name, stamp))
		else:
			print ("이름을 확인해 주세요.")
	def list(self):
		for name in self.attendance:
			print ("이름: %s, 출석일자: %s" % (name, stamp))

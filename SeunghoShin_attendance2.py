import datetime

students = ['seungho shin', 'hyojoon lee', 'jungil yang', 'jarang seo', 'hanseong park']

class Student(object):

	def __init__(self, name):
		self.name = name

class Attendance(object):
	
	attendance = {}
	
	def attend(self, name, date=datetime.date.today().isoformat()):
		if name in students:
			self.attendance[name] = date
		else:
			print ('Check student\'s name !!')

	def list(self):
		for name in self.attendance:
			print ("name: {}, date: {}".format(name, self.attendance[name]))


att = Attendance()

shs = Student('seungho shin')
jgy = Student('jungil yang')
tmy = Student('tommy lee')

att.attend(shs.name)
att.list()

att.attend(jgy.name, '2016-02-22')
att.list()

att.attend(tmy.name)
att.list()

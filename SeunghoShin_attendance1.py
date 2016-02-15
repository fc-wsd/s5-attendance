import datetime

students = ['seungho shin', 'hyojoon lee', 'jungil yang', 'jarang seo', 'hanseong park']

attendances = {}


def attend(name, date=datetime.date.today().isoformat()):
	if studentsListCheck(name):
		attendances[name] = date
		print('%s attends %s.' % (name, date))
		
	else:
		print('Check student\'s name !! [' + name + '] isn\'t student here')

	print('[Attendance List] : %s' % attendances)

def studentsListCheck(name):
	for name_in_list in students:
		if name_in_list == name:
			return True
	return False

attend('seungho shin')
attend('jungil yang', '2016-02-22')
attend('tommy lee')
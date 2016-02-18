from datetime import datetime

students = ['Son', 'Kay', 'Lee', 'Cha', 'Kim', 'Chang', 'Kim', 'Gang',
            'Shin', 'Park', 'Seo', 'Cho', 'Choi', 'Youn']


attendances = {}
def attend(att):
    if att not in students:
        print('There isn\'t \"{}\" in the class.'.format(att))
    else:
        now = datetime.now()
        attendances[att] = '{} came to the class on {}/{}'.format(att,now.month, now.day)


attend('Son')
attend('Kim')
attend('Kay')

print(attendances.values())

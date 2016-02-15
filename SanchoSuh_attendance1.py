students = ['jeongyoon cha', 'sancho suh', 'hyunduk choi', 'seungho shin', 'jonglok kim', 'yongmin kim',
    'hyojoon lee', 'hanjunghyun', 'seunghyun lee', 'jungil yang', 'jarang seo'
]

attendances = {}

def attend(name, attended_at) :
    if studentsValidation(name) :
        attendances[name] = attended_at
        print("log(attend) : succeed in adding attendance to the dictionary")
    else :
        print("log(attend) : " + name + " is not in the student list")


def studentsValidation(name) :
    for l_name in students :
        if l_name == name :
            return True  # Return True if the name is in the student list
    print("log(studentsValidation) : " + name + " is not in the student list")
    return False # else, return False


def printLog() :
    print("Num of attendees : %d" % len(attendances))
    print(attendances)


printLog()
attend('sancho suh', '2016-02-16')
printLog()
attend('Kyungmook Cha', '2016-02-16')
printLog()
attend('hanjunghyun', '2016-02-16')
printLog()

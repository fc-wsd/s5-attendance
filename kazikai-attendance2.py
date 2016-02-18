#author: 한정현
#github id: kazikai
#comments : 20일 수업은 참석 못합니다.. ㅠㅠ
from datetime import date


#Student 클래스
class Student( object ):
    def __init__( self, name ):
        self.name = name
#Attendance 클래스
class Attendance( object ):
    students = [ '김용민', '김종록', '박준영', '박한성', '백성훈', '서인용', '서자랑', '손형우', '신승호', '신호철', '양정일', '윤영식', '이승현', '이효준', '장한별', '조혜연', '차정윤', '최현덕', '한정현' ]
    attendances = []
    def check_student( self, name ):
        if name in self.students:
            return True
        else:
            return False
    def append_student( self, name ):
        self.students.append( name )
    #출석 메소드
    def attend( self, name, date ):
        isCheck = self.check_student( name )
        if isCheck == False:
            print( '새롭게 들어온 학생: ' + name )
            self.append_student( name )
        self.attendances.append({
            'student': Student( name ),
            'date': date
        })
    #출석 확인 메소드
    def list( self ):
        print( '출석에 참여한 학생' )
        for i in self.attendances:
            print( '날짜:' + str( i['date'] ) + ':' + i['student'].name  )
#출석부 생성
attendance = Attendance()

#출석 체크
attendance.attend( '김용민', date.today() )
attendance.attend( '김종록', date.today() )
attendance.attend( '박준영', date.today() )
attendance.attend( '한정현', date.today() )
attendance.attend( '서자랑', date.today() )
attendance.attend( '신호철', date.today() )
attendance.attend( '차경묵', date.today() )
attendance.attend( '차정윤', date.today() )
attendance.attend( '백성훈', date.today() )
attendance.attend( '장한별', date.today() )
attendance.attend( '양정일', date.today() )



#출석부 확인
attendance.list()

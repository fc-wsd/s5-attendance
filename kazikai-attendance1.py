#author: 한정현
#github id: kazikai
#comments : 20일 수업은 참석 못합니다.. ㅠㅠ
from datetime import date
students = [ '김용민', '김종록', '박준영', '박한성', '백성훈', '서인용', '서자랑', '손형우', '신승호', '신호철', '양정일', '윤영식', '이승현', '이효준', '장한별', '조혜연', '차정윤', '최현덕', '한정현' ]
#출석부 생성
attendances = []

def attend( name, date ):
    def check_student( name ):
        if name in students:
            return True
        else:
            return False
    def append_student( name ):
        students.append( name )

    isCheck = check_student( name )
    if isCheck == False:
        print( '새롭게 들어온 학생: ' + name )
        append_student( name )
    attendances.append({
        'name': name,
        'date' : date
    })

#출석 체크
attend( '김용민', date.today() )
attend( '김종록', date.today() )
attend( '박준영', date.today() )
attend( '한정현', date.today() )
attend( '서자랑', date.today() )
attend( '신호철', date.today() )
attend( '차정윤', date.today() )
attend( '차경묵', date.today() )
attend( '백성훈', date.today() )
attend( '장한별', date.today() )
attend( '양정일', date.today() )

#출석부 확인
print( '출석에 참여한 학생' )
for i in attendances:
    print( '날짜:' + str( i['date'] ) + ':' + i['name']  )

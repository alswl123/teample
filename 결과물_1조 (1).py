print ('역사콘텐츠전공 2학기 학사 안내 프로그램입니다.')
print(' ')
print('A. 중간고사')
print('B. 답사 관련')
print('C. 2022학년도 인문사회과학대학 학생회 본선거 투표')
print('D. 학술제, 학술공모전')
print('E. 기말고사')
print('F. 강의평가')
print('G. 종강')
print(' ')
schedule=input('알고자 하는 문자를 하나씩 입력해주세요.(ex_A 혹은 B) :')

if 'A' in schedule or 'a' in schedule:
    print('중간고사기간은 10월 20일 ~ 10월 26일입니다.')

elif 'B' in schedule or 'b' in schedule:
    print('답사 기간은 9월 23일부터 11월 8일까지이고, 답사 공모전은 11월 9일 마감입니다.')

elif 'C' in schedule or 'c' in schedule:
    print('2022학년도 인문사회과학대학 학생회 본선거 투표 기간은 11월 11일 ~ 12일입니다.')

elif 'D' in schedule or 'd' in schedule:
    print('학술제 및 학술공모전은 11월 17일입니다.')

elif 'E' in schedule or 'e' in schedule:
    print('기말고사 기간은 12월 15일 ~ 12월 21일입니다.')

elif 'G' in schedule or 'g' in schedule:
    print('기말 강의 평가 기간은 12월 7일 ~ 12월 30일입니다.')

elif 'F' in schedule or 'f' in schedule:
    print('종강은 12월 22일입니다.')
else:
    print('역사콘텐츠전공 학사 일정이 아닙니다.')

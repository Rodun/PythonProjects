# Section02 - 1

# 1. 기본 출력
print('작은 따옴표')
print("큰 따옴표")
print('''작은 따옴표 x 3''')
print("""큰 따옴표 x 3""")
print() # 내용이 없으면 줄 바꿈

# 2. Separator 옵션 사용
# 작은 따옴표로 감싸진 문자열 사이에 sep의 내용을 추가하여 출력한다.
print('2019', '02', '19', sep='-') 
print('2019', '02', '19')
# e-mail 형식으로 출력
print('niceman', 'google.com', sep='@')

# 3. end 옵션 사용: 줄 바꿈을 하지 않고 다음 문장과 이어준다.
print('Welcome To', end=' ')
print('The Black Paradise', end='')
print('\n')

# 4. format 사용: [대], {중}, (소)
print('{} and {}'.format('You', 'Me'))
print('{0} and {1} and {0}'.format('You', 'Me'))
print("{a} are {b}".format(a='We', b='World'))

# 5. 변환명세: %s 문자열, %d 정수, %f 실수
print("%s %d %f" % ("변환명세 입니다.", 30, 15.5))
# %5d: 5자리의 정수가 온다고 지정, %4.2f: 정수는 4자리, 소수점은 2자리 그리고 실수를 표현
print("Test: %5d, Price: %4.2f" % (776, 12345.34567))
# 키(Dictionary)를 이용하여 format과 변환명세를 함께 사용
print("Test: {0: 5d}, Price:{1: 4.2f}".format(776, 12345.34567))
print("Test: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=12345.34567))

print("\a\a\a\a\a\a\a")

"""
Escape 코드
\n : 개행
\t : 탭
\\ : \ 문자
\' : ' 문자
\" : " 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨소리
\b : 백 스페이스
\000 : 널 문자

"""
# Section02-2

import this # Python 소개글 출력
import sys

# 파이썬 3버전 이후로는 기본 인코딩이 UTF-8 이다.
# 아래는 기본 입출력을 알려줌
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print("My name is AlphaRodun")

# 변수 선언
myName = 'AlphaRodun'

# 조건문
if myName == 'AlphaRodun':
    print('OK')
else:
    print('NO')

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d x %d = ' % (i, j), i * j)

# 들여쓰기 indent는 파이썬의 특징이다.

# 함수
# 함수 선언
def Hello():
    print("Hello i`m AlphaRodun")
# 함수 사용
Hello()

# 클래스
class Cookie:
    pass

# 객체(인스턴스) 생성
_cookie = Cookie()

print(id(_cookie))
print(dir(_cookie))
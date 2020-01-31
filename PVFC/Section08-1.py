# 모듈, 패키지
# 1. 패키지 설정
# 2. 모듈 사용 및 Alias 설정
# 3. 패키지 사용 장점

# 파일 하나의 단위를 모듈: 독립적으로 기능
# 이 파일들을 가지고 있는건 패키지

# 패키지 예제
# (1) 상대 경로
# (1-1) .. : 부모 디렉토리
# (1-2) . : 현재 디렉토리


# 사용 1(클래스)
from pkg.fibonacci import fibonacci

fibonacci.fib(300)
print('ex1: ', fibonacci.fib2(400))
print('ex1: ', fibonacci().title)


# 사용 2(클래스)
from pkg.fibonacci import * # 해당 패키지의 전체 클래스를 가져온다.(메모리 낭비가 심함)


# 사용 3(클래스)
from pkg.fibonacci import fibonacci as fb

fb.fib(1000)
print('ex2: ', fb.fib2(1400))
print('ex2: ', fb().title)

# 사용 4(함수)
import pkg.calculations as cal

print('ex4: ', cal.add(25, 90))
print('ex4: ', cal.mul(10, 120))

# 사용 5(함수)
from pkg.calculations import div as d

print('ex5: ', int(d(100, 10)))

# 사용 6
import pkg.prints as p
import builtins # 기본적으로 사용중인 패키지들

p.prt1()
p.prt2()

print(dir(builtins))


# Python 2.x: 해당 디렉토리가 패키지임을 알리기 위해서는 __init__.py라는
# 빈 파일을 해당 디렉토리에 빈파일로 존재 해야한다.

# Python 3.x: __init__.py가 없어도 작동하지만 3.x 이하의 버전과 호환을 위해서
# 생성해 두는것을 추천한다.

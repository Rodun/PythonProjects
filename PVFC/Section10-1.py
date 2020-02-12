# 에러 및 예외 처리
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로는 에러가 없지만, 코드 실행(런타임)프로세스에서 발생하는 예외 처리도 중요

# linter : 코드 스타일 가이드, 문법 오류 체크


# SyntaxError : 잘못된 문법.
print('Test)

if True
    pass

x => y

# NameError : 참조 변수가 없을때.
a = 10
b = 15
print(c)

# ZeroDivisionError : 0으로 나누려는 에러.
print(10 / 0)

# IndexError : 인덱스 범위가 오버.
x = [10, 20, 30]
print(x[3])

# KeyError
dic = {'name':'kim', 'age':33, 'city':'seoul'}
print(dic['hobby']) # 해당 키가 없어서 에러 발생.
print(dic.get['hobby']) # 해당 키가 없으면 none을 반환. <- 이 방법으로 사용

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
import time
print(time.month()) # 없는 속성을 사용.

# valueError : 참조 값이 없을 때.
x = [1, 5, 9]
x.remove(10)
x.index(10)

# File Not Found Error
f = open('test.txt', 'r')

# Type Error
x = [1, 2]
y = (1, 2)
z = 'test'
print(x + y) # 튜플과 리스트는 서로 결합 할 수 없다.
print(x + list(y) # 형변환을 하면 가능하다.


# (EAFP 코딩 스타일)
# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩을 권장


# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제1 : 예외 발생
name = ['kim', 'lee', 'park']

try:
    z = 'joe'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError: # ValueError만 캐치
    print('not found it - Occurred value Error')


# 예제2 : 모든 에러 캐치
try:
    z = 'jin'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except: # 모든 에러를 캐치
    print('not found it - Occurred value Error')


# 예제3
# else : try문이 정상 실행 되었을때
# finally : 모든 경우에 무조건 실행
try:
    z = 'kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except: # 모든 에러를 캐치
    print('not found it - Occurred value Error')
else:
    print('OK else')
finally:
    print('finally OK')


# 예제4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('try')
finally:
    print('ok finally')


# 예제5
try:
    z = 'kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except IndexError:
    print('not found it - Index Error')
except ValueError:
    print('not found it - value Error')
except Exception:
    print('not found it - Occurred Error')
else:
    print('OK else')
finally:
    print('finally OK')


# 예제6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생
try:
    a = 'kim'
    if a == 'kim':
        print('허가')
    else:
        raise ValueError # 사용자가 직접 지정한 에러
except ValueError:
    print('문제 발생')
except Exception as f:
    print(f)
else:
    print('OK')





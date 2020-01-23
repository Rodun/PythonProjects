# 함수 및 람다(lambda)

# 함수 정의 방법
def f_name():
   return

f_name()

# 예제1
def hello(world):
    print("Hello", world)

hello("Python!!")
hello(7777)

# 예제2
def hello_return(world):
    val = "Hello" + str(world)
    return val

str1 = hello_return(" python~~")
print(str1)

# 예제3 (다중리턴)
def multi_return(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300    
    return y1, y2, y3

val1, val2, val3 = multi_return(3)
print(type(val1), val1, val2, val3)


# 예제4 (iterater 타입 반환)
def multi_return2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300    
    return [y1, y2, y3]
    # return (y1, y2, y3) tuple
    
lt = multi_return2(5)
print(lt, type(lt))


# 예제5
# *args: 가변매개변수 (매개변수의 갯수에 제한을 두지 않는다) 튜플로 넘어온다.
def args_fun(*args):
    print(args)    

args_fun('kim', 'park', 'lee')

def args2_fun(*args):
    for t in args:
        print(t)

args2_fun('kim', 'park', 'lee')

# iterater의 index번호까지 보여준다.
def enum_fun(*args):
    for i, v in enumerate(args):
        print(i, v)
    for i, v in enumerate(range(10)):
        print("[{0}]: {1}".format(i, v))

enum_fun('kim', 'park', 'lee')

# **kwargs: 딕셔너리로 받는 가변매개변수
def kwargs_func(**kwargs):
    print(kwargs)

kwargs_func(name1='kim', name2='lee')

def kwargs2_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

kwargs2_func(name1='kim', name2='lee')


# 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', 'kim', age1=24, age2=30)


# 중첩함수(클로저): 변수의 선언을 줄이거나 메모리관리를 효율적으로 할 수 있다. 
def nested_func(num):
    def func_in_func(num):
        print('>>>', num)
    print('in func')
    func_in_func(num + 100)

nested_func(20)


# 데코레이터: 나중에 다루자


# 예제6: 힌트
def func_hint(x:int) -> list:
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

print(func_hint(5))


# 람다식: 메모리 절약, 가독성 향상(너무 무분별하면 떨어짐), 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(heap 초기화) -> 메모리 초기화

# 일반 함수 -> 변수 할당
def mul_10(num:int) -> int:
    return num * 10

var_func = mul_10 # function이라는 클래스로 선언되어 메모리가 할당 된걸 알 수 있다.
print(type(var_func), var_func, var_func(10))

# 람다식
lambda_mul_10 = lambda num: num * 10
print('>>>', lambda_mul_10(10))

# 함수 매개변수
def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, lambda_mul_10)

print(func_final(10, 10, lambda x : x * 1000))



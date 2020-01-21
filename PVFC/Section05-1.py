#조건문

# bool type
print(type(True))
print(type(False))

# 조건문
# 예1
if True:
    print('yes')

# 예2
if False:
    print('no')

# 예3
if False:
    print('no2')
else:
    print('yes2')

# 관계연산자
# >, >=, <. <=, ==, !=

A = 10
B = 5

print(A > B)
print(A >= B)
print(A < B)
print(A <= B)
print(A == B)
print(A != B)

# bool type이 아닌 type의 참, 거짓 구분
# 참: "내용", [내용], (내용), {내용}, 1
# 거짓: "", [], (), {}, 0

StrTest = "hi"
StrTest2 = ""

if StrTest:
    print(StrTest)

if StrTest2:
    print("Not Empty")
else:
    print("Is Empty")


# 논리연산자
# and, or, not

C = 100
D = 60
E = 15

print('and: ', C > D and D > E)
print('or: ', C > D or E > D)
print('not: ', not C > D)
print(not False)
print(not True)

# 산술, 관계, 논리 연산자
# 산술 > 관계 > 논리의 순서로 적용된다.

print('ex1: ', 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print('PASS')
else: 
    print('FAIL')

# 다중조건문
num = 90

if num >= 90:
    print('A')
elif num >= 80:
    print('B')
elif num >= 70:
    print('C')
else:
    print('F')

# 중첩조건문
age = 27
height = 178

if age >= 20:
    if height >= 170:
        print('해병대 가능')
    elif height >= 160:
        print('해군 가능')
    else:
        print('지원불가')
else:
    print('20세 이상 지원 가능')

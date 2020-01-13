# Python Data Type List

# Boolean
# Numbers
# String
# Bytes

# 집합 자료형
# - Lists
# - Tuples
# - Sets
# - Dictionaries

v_str1 = 'Niceman'
v_bool = True
v_str2 = "Good Boy"
v_float = 8.7
v_int = 22
v_dict = {
    "name" : "Kim",
    "age" : 17,
    "run" : True
}
v_list = [1, 2, 3]
v_tuple = 4, 5, 6
v_set = {7, 8, 9}


# 현재 데이터의 타입 출력
print(type(v_str1))
print(type(v_bool))
print(type(v_str2))
print(type(v_float))
print(type(v_int))
print(type(v_dict))
print(type(v_list))
print(type(v_tuple))
print(type(v_set))

F2 = 7.5
I1 = 10

result = F2 + I1
print(result, type(result))


# 형변환
# int, float, complex(복소수)

c = 3
print(int(result))
print(float(c))
print(complex(5))
print(int(True))
print(int("33"))
print(complex(False))


# 단항연산자
y = 100
y += 100
print(y)

y *= 2
print(y)

# 수치 연산 함수
# https://docs.python.org/3/library/math.html <- 파이썬의 모든 수학 함수

print(abs(-4)) # 절대값
n, m = divmod(100, 8) # 100을 8로 나눠서 몫을 n에 나머지를 m에 넣어준다.
print(n, m)

import math

print(math.ceil(5.1)) # 5.1보다 크면서 가장 작은 정수를 출력
print(math.floor(3.777)) # 3.777보다 작으면서 가장 큰 정수 출력




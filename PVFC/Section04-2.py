# 문자열, 문자열 연산, 슬라이싱

str1 = "i am a boy"
str2 = 'nice man'
str3 = ''
str4 = str()

print(len(str1), len(str2), len(str3), len(str4)) # 문자열의 길이


# 이스케이프 문자
escape_str1 = "Do you have an \"apple\"?"
print(escape_str1)
escape_str2 = "Tab\tTab\tTab\t"
print(escape_str2)

# Raw String: 문자열 사이의 이스케이프문 무시
raw_s1 = r'C:\Programs\test\number\bin'
print(raw_s1)
raw_s2 = r"\\a\a"
print(raw_s2)

# 멀티라인: 변수 선언 바로 다음에 "\" 를 입력하면 다음줄 부터 있다고 알림
multi_s = \
""" 
문자열 
멀티라인 
1 
"""
print(multi_s)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = "def"
str_o4 = "Niceman"

print(str_o1 * 20)
print(str_o2 + str_o3)
print(str_o1 + str(3))
print('a' in str_o4) # 'a'가 str_o4에 포함 되었는지?
print('z' not in str_o4) # 위와 반대

# 문자열 형 변환
print(str(88) + 'a')
print(str(10.4))

# 문자열 함수
# 참고: https://www.w3schools.com/python/python_ref_string.asp

a = 'niceman'
b = 'Orange'

print(b.islower()) # 문자열 전체가 소문자 인지?
print(b.endswith('e')) # 마지막 문자가 'e'인지?
print(a.capitalize()) # 첫글자를 대문자로 바꾸어준다.
print(a.replace('nice', 'good')) # 문자열 바꾸기
print(list(reversed(b))) # 문자열의 순서를 뒤집어 list로 만들어준다.


# 문자열은 할당이 되면 변경이 안된다.

print(a[0:3]) # 0부터 3개
print(a[0:len(a)]) # 전체
print(a[:4]) # 처음부터 4까지
print(a[:])  # 전체

print(b[0:4:2]) # 0 다음의 2칸을 스킵
print(b[1:-2])
print(b[::-1])
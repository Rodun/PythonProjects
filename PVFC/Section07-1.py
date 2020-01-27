# 파이썬 클래스 상세 이해
# Self, Class, Instance 변수

# 선언
'''
class 클래스명:
    함수
    함수
    변수
'''

# 예제1
# 클래스의 구성: 속성, 메소드(방법, 동작)
class UserInfo:
    def __init__(self, name):
        self.name = name
        print('Initailize')
    
    def user_info(self):
        print('Name:', self.name)


user1 = UserInfo('홍길동')
user1.user_info()

print(id(user1))
print(user1.__dict__)



# 파이썬 클래스 상세 이해
# Self, Class, Instance 변수

# 클래스와 인스턴스의 차이
# 네임스페이스: 각각의 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수: 직접 사용 가능, 객체보다 먼저 생성된다.
# 인스턴스 변수: 객체마다 별도로 존재한다, 인스턴스 생성 후 사용한다.

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

user2 = UserInfo('이순신')
user2.user_info()
print(id(user2))
print(user2.__dict__)

# 예제2
# self의 이해
class SelfTest():
    def __init__(self):
        pass

    def function1(): # self 매개변수가 없다면 클래스 메소드로써 사용하게 된다.
        print('function1 called')

    def function2(self):
        print(id(self))
        print('function2 called')


self_test = SelfTest()

SelfTest.function1() # 클래스 메소드 사용 -> 클래스를 직접사용하는 모습

self_test.function2()
print(id(self_test)) # function2 내부의 print(id(self))와 비교하면 같다는 것을 알 수 있다.
SelfTest.function2(self_test)

# 예제3
# 클래스 변수, 인스턴스 변수(self를 사용해아한다)

class WareHouse:
    # 클래스 변수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1


user_1 = WareHouse('Kim')
user_2 = WareHouse('Park')
user_3 = WareHouse('Lee')

print(user_1.__dict__)
print(user_2.__dict__)
print(user_3.__dict__)
print(WareHouse.__dict__) # 클래스 네임스페이스

print(user_1.name)
print(user_2.name)
print(user_3.name)

print(user_1.stock_num) # 클래스 변수(공유)

del user_1 # 소멸자를 이용하여 stock_num의 수를 줄이고 아래 user2를 통해서 클래스 변수를 출력
print(user_2.stock_num)
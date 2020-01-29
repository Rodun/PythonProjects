# 클래스 상속, 다중 상속

# 예제1
# 상속 기본
# 슈퍼클래스(부모)의 서브클래스(자식)은 부모의 모든 속성, 메소드를 사용 가능

# 라면 -> 속성(종류, 제조사, 맛, 면, 이름) : 부모

class Car:
    '''Parent(Super) Class'''
    def __init__(self, _type, _color):
        self.type = _type
        self.color = _color

    def show(self):        
        return 'car class "Show Method!"'


class BMW_Car(Car):
    '''Children(Sub) Class'''
    def __init__(self, _name, _type, _color):
        super().__init__(_type, _color)
        self.name = _name

    def show_model(self) -> None: # -> None는 Return값이 없다는 의미
        return "Your Car Name: %s" % self.name


class Benz_Car(Car):
    '''Children(Sub) Class'''
    def __init__(self, _name, _type, _color):
        super().__init__(_type, _color)
        self.name = _name

    def show_model(self) -> None: # -> None는 Return값이 없다는 의미
        return "Your Car Name: %s" % self.name

    def show(self):
        print(super().show()) # Super Method Call
        return 'Car Info : %s %s %s' % (self.name, self.type, self.color)


# 일반 사용
model1 = BMW_Car('520d', 'sedan', 'red')
print(model1.color) # super
print(model1.type) # super
print(model1.name) # sub
print(model1.show()) # super
print(model1.show_model()) # sub
print(model1.__dict__, end='\n\n')

# Method Overriding(오버라이딩): 부모에 있는 메소드를 자식에서 변형시켜 사용할 수 있다.
model2 = Benz_Car('220d', 'suv', 'black')
print(model2.show()) # super
print(model2.show_model()) # sub
print(model2.__dict__, end='\n\n')

# Super Method Call
model3 = Benz_Car('350s', 'sedan', 'silver')
print(model3.show())

# Inheritance Info (상속 정보)
print(BMW_Car.mro()) # mro()는 클래스의 상속 관계를 알려준다.
print(Benz_Car.mro())
print(end='\n\n')

# 예제2
# 다중 상속

class X():
    pass

class Y():
    pass

class Z():
    pass

class XY(X, Y):
    pass

class YZ(Y, Z):
    pass

class YZ_XY_Z(YZ, XY, Z):
    pass

# 너무 복잡한 다중 상속은 코드를 해석하기 어렵게 만든다.
print(YZ_XY_Z.mro(), end='\n\n')

print(XY.mro())

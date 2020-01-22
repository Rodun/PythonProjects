# 코딩의 핵심은 조건을 해결하는것
# 기본 반복문: for, while

# while
v1 = 1
while v1 < 11:
    print("v1:", v1)
    v1 += 1

for v2 in range(10):
    print("v2:", v2)

for v3 in range(1, 11):
    print("v3:", v3)

# 1~100까지의 합
sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print("1~100 합:", sum1)
print("1~100 합(range):", sum(range(1, 101)))
print("1~100 짝수의 합(range):", sum(range(1, 101, 2)))

# 시퀀스 자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리
# iterable return function : range, reversed, enumerate, filter, map, zip

names = ['kim', 'park', 'joe', 'choi', 'yoo']
for name in names:
    print('Name:', name)

words = "Strawberry"
for word in words:
    print(word, end=' ')
print()

my_info = \
{
    'name' : 'kim',
    'age' : 19,
    'city' : 'seoul'
}

for source in my_info:
    print(source, end=' ')
print()

for source in my_info.keys():
    print(source, end=' ')
print()

for source in my_info.values():
    print(source, end=' ')
print()

for source in my_info.items():
    print(source, end=' ')
print()

for k, v in my_info.items():
    print('[key:', k, ',value:', v, end='] ')
print()

name2 = 'AlphaRODUN'
for n in name2:
    if n.isupper():
        print(n.lower(), end='')
    else:
        print(n.upper(), end='')

# break
numbers = [45, 66, 12, 7, 33, 97, 31, 78, 25, 51, 23]
for num in numbers:
    if num == 33:
        print('Found:', num)
        break
    else:
        print('not found')

# for - else: 반복할 동안 중간에 break를 만나지 않고 끝까지 수행된 경우 for - else를 실행하게 된다.
for num in numbers:
    if num == 33:
        print('Found:', num)
    else:
        print('not found')
else: # for - else
    print('for is end')

# continue
lt = ['str', 2, 3, True, 4.5, complex(4)]
for v in lt:
    if type(v) is float:
        continue
    print(v, '타입:', type(v))
        
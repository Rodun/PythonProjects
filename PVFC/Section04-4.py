# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형


# Dictionary: 순서x, 중복x, 수정o, 삭제o
# Key(정보), Value(값)

# 선언
DtA = { 'name':'Kim', 'phone':'010-1234-1234', 'birth':'200101' }
DtB = { 0 : 'hello python', 1 : 'hello coding' }
DtC = { 'arr' : [1, 2, 3, 4] }

# 출력
print(DtA['name'])
print(DtA.get('name')) # get을 이용하여 조회를 하면 해당 Key가 존재하지 않더라도 에러를 발생하지 않는다.
print(DtC['arr'][1:3])

# 추가
DtA['address'] = 'seoul'
print(DtA['address'])
DtA['rank'] = [1, 2, 3]
DtA['rank2'] = (4, 5, 6)
print(DtA)

# keys, values, items
print(DtA.keys()) # keys
Temp_List = list(DtA.keys())
print(Temp_List[1])
print(Temp_List[1:3])

print(DtA.values()) # values

print(DtA.items()) # items



# Set 집합: 순서x, 중복x
SA = set()
SB = set([1, 2, 3])
SC = set([3, 4, 1, 2, 2])

print(SC) # 중복은 제외하고 출력됨

t1 = tuple(SB)
print(t1)

l1 = list(SB)
print(l1)

S1 = set([1, 2, 3, 4, 5, 6])
S2 = set([4, 5, 6, 7, 8, 9])

print(S1.intersection(S2)) # 교집합
print(S1 & S2) # 교집합

print(S1 | S2) # 합집합
print(S1.union(S2)) # 합집합

print(S1 - S2) # 차집합
print(S1.difference(S2)) # 차집합

# 추가, 제거
S3 = set([7, 8, 10, 15])
S3.add(18)
print(S3)

S3.remove(15)
print(S3)
# Section04-3
# List, Tuple

# List: 순서(O), 중복(O), 수정(O), 삭제(O)

# 선언
ListA = []
ListB = list()
ListC = [1, 2, 3, 4]
ListD = [10, 100, 'Pen', 'Banana', 'Orange']
ListE = [20, 30, ['Lion', 'Tiger',], [ [60, 70], [80, 90]] ]
print(ListA, ListB, ListC, ListD, ListE, sep='\n')

# 인덱싱
print(ListD[3], ListD[-2], sep='\n')
print(ListD[0] + ListD[1])
print(ListE[2][1])
print(ListE[-2][0])

# 슬라이싱
print(ListD[0:3])
print(ListE[2][:2])

# 연산
print(ListC + ListE)
print(ListC * 3)
print(str(ListC[0]) + ' + Hi')

# 수정
ListC[0] = 77
print(ListC[0])
ListC[1:2] = [100, 1000, 10000]
print(ListC)
ListC[1] = ['a', 'b', 'c']
print(ListC)

# 삭제
del ListC[1]
print(ListC)
del ListC[-1]
print(ListC)

# List 함수
list_y = [5, 2, 3, 4, 1]
print(list_y)

list_y.append(6) # 끝 부분에 삽입
print(list_y)

list_y.sort() # 오름차순으로 정렬
print(list_y)

list_y.reverse() # 현재 순서를 뒤집는다.
print(list_y)

list_y.insert(2, 7) # 특정 인덱스 위치에 삽입
print(list_y)

list_y.remove(2) # 특정 값을 찾아서 제거
del list_y[2] # 해당 인덱스를 제거
print(list_y)

# 맨 마지막 원소를 꺼내면서 제거한다. LIFO: Last In First Out
# pop을 계속 돌리면 결국 리스트의 원소가 모두 없어져 에러를 발생 시킬수 있기 때문에 주의 하여야 한다.
list_y.pop() 
print(list_y)

# 끝 부분에 해당 리스트를 연장하여 준다. 
# append는 리스트 안에 원소로 리스트가 들어가지만 extend는 현재 리스트를 확장해준다.
# ly = [3, 4]
# list_y.append(ly) -> [1, 2, [3, 4]]
# list_y.extend(ly) -> [1, 2, 3, 4]
ly = [88, 77]
list_y.extend(ly) 
print(list_y)
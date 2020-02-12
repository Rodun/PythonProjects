# 파일 Read, Write
# https://docs.python.org/3.7/library/functions.html#open

# 읽기 모드 : r
# 쓰기 모드 : w (기존 파일 삭제)
# 추가 모드 : a (파일 생성 또는 추가)

# 파일 읽기
# 예제 1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
# open을 하였으면 반드시 close로 리소스를 반환해야 한다.
f.close()

print('==================\n')

# 예제2
# with문은 close를 하지 않아도 with문이 끝나면 자동으로 닫아준다.
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print('==================\n')

# 예제3
with open('./resource/review.txt', 'r') as f: # f가 iterable 이다
    for c in f:
        print(c.strip()) # str.strip()을 사용하면 양쪽 공백과 줄바꿈을 제거해준다.

print('==================\n')

# 예제4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)

    # 한 번 읽어오게 되면 해당 파일에서 커서가 맨 끝으로 이동 되기 때문에 
    # 다시 읽어도 끝에만 읽어서 내용이 없다.
    content = f.read() 
    print(">", content)

print('==================\n')

# 5. readline()
with open('./resource/review.txt', 'r') as f:
    line = f.readline()    
    while line:
        print(line, end='^^^')
        line = f.readline()

print('==================\n')

# 6. readlines()
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines() # 이스케이프문(줄바꿈 같은)을 포함해서 리스트 형태로 가져온다.   
    print(contents)
    for c in contents:
        print(c, end='!!!')

print('==================\n')

# 예제7
score = list()
with open('./resource/score.txt', 'r') as f:    
    for line in f:
        score.append(int(line))
    print(score)

print('Average : {:6.3}'.format(sum(score) / len(score)))



# 파일 쓰기

# 예제1
with open('./resource/text1.txt', 'w') as f: # 쓰기 모드 : w (기존 파일 삭제)
    f.write('Niceman!2')

# 예제2
with open('./resource/text1.txt', 'a') as f: # 추가 모드 : a (파일 생성 또는 추가)
    f.write('\nGood man!')


# 예제3
from random import randint
with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 45)))
        f.write('\n')

# 예제4
# writelines : 리스트를 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list = ['kim\n', 'park\n', 'joe\n']
    f.writelines(list)

# 예제5
with open('./resource/text4.txt', 'w') as f:
    print('Test Contents!', file=f) # print를 이용하여 파일로 저장.
    
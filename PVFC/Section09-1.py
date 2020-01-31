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

print('==================')

# 예제2
# with문은 close를 하지 않아도 with문이 끝나면 자동으로 닫아준다.
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print('==================')

# 예제3
with open('./resource/review.txt', 'r') as f: # f가 iterable 이다
    for c in f:
        print(c.strip()) # str.strip()을 사용하면 양쪽 공백과 줄바꿈을 제거해준다.

print('==================')

# 예제4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)

    # 한 번 읽어오게 되면 해당 파일에서 커서가 맨 끝으로 이동 되기 때문에 
    # 다시 읽어도 끝에만 읽어서 내용이 없다.
    content = f.read() 
    print(">", content)

print('==================')

# 5. readline()
with open('./resource/review.txt', 'r') as f:
    line = f.readline()    
    while line:
        print(line, end='^^^')
        line = f.readline()

print('==================')

# 6. readlines()
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines() # 이스케이프문(줄바꿈 같은)을 포함해서 리스트 형태로 가져온다.   
    print(contents)
    for c in contents:
        print(c, end='!!!')

print('==================')

# 예제7
with open('./resource/score.txt', 'r') as f:
    score = list()
    for line in f:
        score.append(int(line))
    print(score)



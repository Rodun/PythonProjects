# Excel, CSV 파일 읽기, 쓰기
# 파이썬 외부 파일 처리

# CSV : MIME - text/csv
import csv

# 1-1) 읽기
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # 한 줄 단위로 넘길수 있다. (header skip)

    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)


# 1-2) delimiter 구분자
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|') # delimiter : 구분자를 알려준다.

    for c in reader:
        print(c)


# 1-3) Dict 변환
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        print(c)















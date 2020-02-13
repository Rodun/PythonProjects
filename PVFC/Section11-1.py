# Excel, CSV 파일 읽기, 쓰기
# 파이썬 외부 파일 처리

# 1. CSV : MIME - text/csv
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


# 1-3) Dict 변환 : 첫번째 줄의 내용을 키로 지정하여 Dictionary를 만들어준다.
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k, v)            
        print('------------------')


# 1-4) csv 파일 작성
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

# 자동으로 줄바꿈을 해주는데 newline를 사용하면 줄 바꿈에 대한 설정을 할 수 있다.
with open('./resource/sample4.csv', 'w', newline='') as f: 
    wt = csv.writer(f)
    for v in w:
        wt.writerow(v)


# 1-5) writerows : 한번에 입력하기
with open('./resource/sample5.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)


# 2. XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas를 주로 사용한다.(openpyxl, xlrd)

# cmd에서 아래 3가지 설치
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd

xlsx = pd.read_excel('./resource/sample.xlsx')
# read_excel의 옵션 : https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html?highlight=to_excel
# xlsx = pd.read_excel('./resource/sample.xlsx', 옵션명=값)
# ex1) sheetname='시트명 or 숫자'
# ex2) header=3
# ex3) skiprow='숫자' -> 해당 row를 가져오지 않는다.

# 상위 데이터 확인 : 상위 5개 출력
print(xlsx.head())

# 데이터 확인 : 하위 5개 출력
print(xlsx.tail())

# 구조 파악 : 행, 열
print(xlsx.shape)

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)





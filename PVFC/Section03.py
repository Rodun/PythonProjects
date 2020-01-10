# Section03
# 외부 설치 패키지 테스트

import simplejson as json

test_dict = {'1':99, '4':77, '3':65, '5':100, '2':88}

# simplejson 실행
print(json.dumps(test_dict, sort_keys=True, indent=4*' '))
print(test_dict)
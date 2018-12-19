# 181218 수업정리

## 1. 개발환경 설정

* chocolatey
  * 윈도우 패키지 매니저
* python -v3.6.7
* git
  * version Control System
* vscode
  * Code Editor
* chrome
  * Browser

## 2. list

### list 만들기

```python
mcu = [
    ['ironman', 'captain america', 'dr.strange'],
    ['xmen', 'deadpool'],
    ['spiderman']    
]

disney = mcu[0]
dr_strange = disney[2]
dr_strange = mcu[0][2]
```

이때  `'dr.strange'`에 접근하려면 어떻게 해야할까?

리스트 안에 리스트가 있다!

### list 추출하기

1. `[0]` 처럼 인덱스 접근하기
2. `[1:10]` 처럼 잘라내기
3. `[start:end]` start는 포함,  end는 안 포함!

### list 연산

```python
team = [
    'john',
    10000,
    'neo',
    100,
    'tak',
    40500
]

type(team[2:4]) #하나든 여러개든 슬라이싱한 값은 list

new_member = ['js', 10]

team = team + new_member #list 끼리 덧셈연산은 list안에 list가 들어가는 것이 아니라 list끼리 한 list로 합쳐짐
team += new_member
```

cf) += 등호기호가 같이 있는 경우 항상 =이 뒷쪽에 온다.

### 3. dict

```python
hphk = [
    {
        'name':'john',
        'email':'john@hphk.io'
    },
    {
        'name':'neo',
        'email':'noe@hphk.kr'
    },
    {
        'name':'tak',
        'email':'tak@hphk.io'
    }
]

p = hphk[2]
type(hphk) #list
type(p) # dict

print(p['name'])
hphk[2]['name']
```

이때  `'tak'`에 접근하려면 어떻게 해야할까?

리스트 안에 딕셔너리가 있다!

딕셔너리 안에 또 딕셔너리가 있을 수 있다.

cf) 딕셔너리는 `'KEY':'VALUE'`형태로 존재

입력할 때는 {}, 불러올 때는 []

### 4. function

```python
scores = [45, 60, 78, 88]
higt_score = max(scores) #최대값
lowest_score = min(scores) #최소값 min([]), min(1,2) 최소 2개 이상의 숫자
round(1.8) #2
round(1.4) #1 =>반올림
round(1.876, 2) # 소숫점 둘째자리까지 반올림


first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

#full에 first 와 second 을 합쳐서 저장
full = first + second

#full_sorted에 full을 오름차순으로 정렬하여 저장
full_sorted = sorted(full)

#reverse_sorted 에 full을 내림차순으로 정렬하여 저장
reverse_sorted = sorted(full, reverse=True)
```



### 5. method

메서드는 함수다! 다만 **[주어],** **동사()** 의 형식으로 이루어 지며,  [주어] 자리에 오는  object들이 할 수 있는 행동(함수)들이다.

```python
my_list = [4, 7, 9, 1 ,3, 6]
# 최대/최소
max(my_list)
min(my_list)
#특정 요소의 인덱스. mY_list에서 한 요소가 몇번째에 있는지?
my_list.index()
#리스트를 뒤집으려면?
my_list.reverse()


dust = 100 # <class: int>
language = 'python' # str
samsung = ['elec', 'sds', 's1'] # list
# method란 object에 속해있는 함수, object가 할 수 있는 행동

language.capitalize() #맨 앞글자 대문자로
language.replace('on', 'off') # on을 off로 바꿔라
'python'.index('o')

samsung.index('sds')
samsung.count('s1') # s1이 몇 개 들어있는가

#보통은 뒤에 메소드를 작성해도 원본이 유지되나
#유지되지 않고 원본이 바뀌는 경우도 있다. ex) .sort()
numbers = [9, 5, 8, 1, 2]
sorted_numbers = numbers.sort()

samsung + ['bio']
samsung.append('bio') #뒤에 내용 붙임. 원본이 바뀜!!

```

| str        | int   | list             | bool      | <==class  |
| ---------- | ----- | ---------------- | --------- | --------- |
| `'python'` | `100` | `['a', 3, True]` | `'False'` | <==object |

### 6. web browser

```python
import webbrowser

keywords = [
    'bts', 
    'python', 
    'SSAFY'
]

for keyword in keywords:
    url = 'https://www.google.com/search?q=' + keyword
    webbrowser.open_new(url)

```



### 7. lotto

1. pick lotto number

```python
import random

numbers = list(range(1, 46))

my_numbers = random.sample(numbers, 6)

print(my_numbers)

print(random.sample(list(range(1, 46)), 6))
```

2. get lotto data

```python
import requests
#{   
#    "drwtNo1":2
#    "drwtNo2":25,
#    "drwtNo4":30,
#    "drwtNo5":33,
#    "drwtNo6":45,
#    "bnusNo":6,}

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)
lotto_data = response.json()


real_numbers = []

# for key in lotto_data:  # in 뒤의 lotto_data가 ㅇㅇ인경우? key값이 나옴
#     if 'drwtNo' in key:
#         real_numbers.append(lotto_data[key])

for key, value in lotto_data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)

real_numbers.sort()
bonus_number = lotto_data['bnusNo']
print(real_numbers)
```



### 8. weather

```python
from darksky import forecast

multicampus = forecast('a11e9488156cceaddf3805cad9ea8cb4', 37.501554, 127.03966)

print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])

```

pip install darkskylib 입력하여 설치 => python -m pip install --upgrade pip 입력하여 업데이트

Dark Sky API 에서 위치 정보 & 구글지도에서 위도경도 위치 확인

cf) [PyPI – the Python Package Index · PyPI](https://pypi.org/)에 있는 파일은 vscode에서 입력하여 설치 가능


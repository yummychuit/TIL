# 181220 수업정리

HTML, CSS 

## 1. HTML

`<h1>`은 가.장. 중요한 제목, 문서에서 한 번만 사용 

단순히 사이즈로 지정하는 것이 아님. 제목의 중요성?을 표현하는 것

사이즈를 조정하고 싶다면 사이즈 시트에서 조절하면 됨

(브라우저 세팅에서 사이즈나 굵기 등 조절할 수 있음)

`<div>`는 가상의 네모 만드는 것. 공간을 나누는 역할.

mark up => 역할을 정해주는 것

`<br>` 

## 2. 

client side에서 client 역할을 하는 가장 친숙한 프로그램 - 브라우저 , 앱



### 3. 지난과제 로또 + function

```python
#기능단위로 나누기

import random
import requests

def pick_lotto(): #정의 #순서의 영향을 받음 #함수 정의는 윗쪽에 쓰는것이 좋음
    numbers = set(random.sample(range(1, 46), 6)) #굳이 list(range(1, 46))라고 list로 캐스팅 하지 않아도 정수로 처리됨
    return numbers #함수는 return을 하거나 아무것도 retrun하지 않거나 둘 중 하나다. 


my_numbers = pick_lotto()
print(my_numbers) #None이 프린트되면=> 아무것도 없다는 뜻. *동작하지 않는다는 것이 아님!!!!!* return값이 없는 것.

real_numbers = get_lotto(837) #여기서 회차 숫자 바꾸면 다른 회차 번호도 나옴
print(real_numbers)


def am_i_lucky(pick, draw):
    
    match_count = len(set(pick) & set(draw['numbers']))


    if match_count == 6:
        print('1등')
    elif match_count == 5 and bonus in my_numbers:
        print('2등')
    elif match_count == 5:
        print('3등')
    elif match_count == 4:
        print('4등')
    elif match_count == 3:
        print('5등')
    else : print('꽝')


am_i_lucky(my_numbers, real_numbers)




```

```python
#1단계! 간단한 문제로 먼저 이해하며 풀어보자!
#내가 품
list_1 = [1, 2, 3, 4, 5, 6]

list_2 = [1, 2, 3, 4, 5, 7]
bonus = 6

def am_i_lucky(pick, draw):
    print(pick)
    print(draw)

    match_no = len(set(pick) & set(draw))

    if match_no == 6:
        print('1등')
    elif match_no == 5 and bonus in list_1:
        print('2등')
    elif match_no == 5:
        print('3등')
    elif match_no == 4:
        print('4등')
    elif match_no == 3:
        print('5등')
    else : print('꽝')

am_i_lucky(list_1, list_2)

#선생님 풀이

def am_i_lucky(pick, draw):
    match = set(pic) & set(draw)
    if len(match) == 6:
        return('1등')
    elif len(match) ==5:
        return('3등')
    else: 
        return('꽝') #return이 여러개여도 동시에 실행되지 않음. 하나만 실행됨

result = am_i_lucky([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 7])
print(result)


# list_1 = [1, 2, 3, 4, 5, 6]
# dict_1 = {
#     'numbers': [1, 2, 3, 4, 5, 6],
#     'bonus': 7
# }



def am_i_lucky(pick, draw):
    match = set(pick) & set(draw['numbers'])
    if len(match) == 6:
        return('1등')
    elif match_no == 5 and draw['bonus'] in pick:
        return('2등')
    elif len(match) ==5:
        return('3등')
    else: 
        return('꽝')

# am_i_lucky(list_1, dict_1)
am_i_lucky(pick_lotto, get_lotto(837))
print(result)
```









```python
#cf
#컨벤션 - 법칙은 아니지만 지키는 것. 관습법 같은 것.
#리펙토링 - 이름을 적절하게 지어주는 것? 기능이 바뀌거나 성능이 바뀌는 것은 없지만 더 나아지게 코드를 바꿔주는 것.
#arguments - 인자(args) 괄호안에 인자로 들어오는 것.

# cf
a = sorted([3, 2, 1])
def sorted():
    sdlskdj
    dkjsld
    return akd

b = [3, 2, 1].sort()
def sort():
    aldkaljdlk
    aldkjlfja
    aldjlfaj

# 인자가 있고 리턴이 있다. => yes in yes out
# 인자가 있고 리턴이 없다. => yes in no out
# 인자가 없고 리턴이 있다. => no in yes out
# 인자가 없고 리턴이 없다. => no in no out


```



# #{   
# #    "drwtNo1":2
# #    "drwtNo2":25,
# #    "drwtNo4":30,
# #    "drwtNo5":33,
# #    "drwtNo6":45,
# #    "bnusNo":6,}

# url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

# response = requests.get(url, verify=False)
# lotto_data = response.json()


# real_numbers = []

# # for key in lotto_data:  # in 뒤의 lotto_data가 ㅇㅇ인경우? key값이 나옴
# #     if 'drwtNo' in key:
# #         real_numbers.append(lotto_data[key])

# for key, value in lotto_data.items():
#     if 'drwtNo' in key:
#         real_numbers.append(value)

# real_numbers.sort()
# bonus_number = lotto_data['bnusNo']
# print(real_numbers)



# numbers = list(range(1, 46))

# my_numbers = random.sample(numbers, 6)

# print(my_numbers)

# my_numbers, real_numbers, bonus_number
# 1등 : my_numbers == real_numbers
# 2등 : eal_numbers & my_numbers 가 5개가 같고, 나머지 하나의 my_numbers == bonus_number
# 3등 : real_numbers & my_numbers 가 5개가 같다
# 4등 : real_numbers & my_numbers 가 4개가 같다
# 5등 : real_numbers & my_numbers 가 3개가 같다
# 꽝


# import random
# import requests
#{   
#    "drwtNo1":2
#    "drwtNo2":25,
#    "drwtNo4":30,
#    "drwtNo5":33,
#    "drwtNo6":45,
#    "bnusNo":6,}

# url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

# response = requests.get(url, verify=False)
# lotto_data = response.json() #url 받아오기

# real_numbers = []
# for key, value in lotto_data.items():
#     if 'drwtNo' in key:
#         real_numbers.append(value)

# real_numbers.sort()
# bonus_number = [lotto_data['bnusNo']] #로또정보 sort

# numbers = list(range(1, 46))
# my_numbers = random.sample(numbers, 6)
# print('내 번호: ', my_numbers) #로또정보 뽑기


# my_numbers = [1, 2, 3, 4, 5, 6]
# real_numbers = [1, 2, 3, 4, 5, 6]
# bonus_number = [7]

# same_numbers = list(set(my_numbers).intersection(real_numbers))
# num_same_num = len(same_numbers)
# exc_same = list(set(my_numbers).difference(real_numbers))
# exc_bonus = list(set(exc_same).intersection(bonus_number))

# if num_same_num == 6:
#     print("으아항아ㅏ으아앙 1등입니다!!!!!")
# elif num_same_num == 5:
#     if exc_bonus == []:
#         print("오오오옼 3등입니다!!!")
#     else:
#         print("우와아ㅏㅇ아아 2등입니다!!!!")
# elif num_same_num == 4:
#     print("우오 4등입니다!!")
# elif num_same_num == 3:
#     print("오 5등입니다!")
# else: print("꽝.....ㅠㅠ")


# count = 0
# for my_number in my_numbers:
#     for real_number in real_numbers:
#         if my_number == real_number:
#             count += 1
# print('동일한 숫자 개수: ', count)

# if count == 6:
#     print(1)
# elif count == 5 and bonus in my_numbers:
#     print(2)
# elif count == 5:
#     print(3)
# elif count == 4:
#     print(4)
# elif count == 3:
#     print(5)
# else : print('꽝')


# # list = [1, 2, 3]
# # tuple = (1, 2, 3) #list와 tuple이 비슷 
# # set = {1, 2, 3} #순서가 없다

# my_numbers = set([1, 2, 3, 4, 5, 6]) #set으로 변환
# real_numbers = set([1, 2, 3, 4, 5, 6])
# bonus_number = 7

# match_count = len(my_numbers & real_numbers)
# print(match_count)

# if match_count == 6:
#     print('1등')
# elif match_count == 5 and bonus in my_numbers:
#     print('2등')
# elif match_count == 5:
#     print('3등')
# elif match_count == 4:
#     print('4등')
# elif match_count == 3:
#     print('5등')
# else : print('꽝')


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


#기능단위로 나누기

import random
import requests


def pick_lotto(): #정의 #순서의 영향을 받음 #함수 정의는 윗쪽에 쓰는것이 좋음
    numbers = random.sample(range(1, 46), 6) #굳이 list(range(1, 46))라고 list로 캐스팅 하지 않아도 정수로 처리됨
    return numbers #함수는 return을 하거나 아무것도 retrun하지 않거나 둘 중 하나다. 

my_numbers = pick_lotto()
print(my_numbers) #None이 프린트되는 것=> 아무것도 없다는 뜻. 동작하지 않는다는 것이 아님!!!!! return값이 없는 것.


def get_lotto(draw_no):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+ str(draw_no) #draw_no는 정수기 때문에 string 처리 해줌

    response = (requests.get(url))
    lotto_data = response.json()
    
    numbers = []
    for key, value in lotto_data.items():
        if 'drwtNo' in key:
            numbers.append(value)

    numbers.sort()
    bonus_number = lotto_data['bnusNo']
    # { numbers: [1, 2, 3, 4, 5, 6], bonus: 7 }
    final_dict = {
        'numbers': numbers,
        'bonus' : bonus_number
    }
    return final_dict

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



#cf) 컨벤션 - 법칙은 아니지만 지키는 것. 관습법 같은 것.
# 리펙토링 - 이름을 적절하게 지어주는 것? 기능이 바뀌거나 성능이 바뀌는 것은 없지만 더 나아지게 코드를 바꿔주는 것.
#arguments - 인자(args) 괄호안에 인자로 들어오는 것.

# 인자가 있고 리턴이 있다. => yes in yes out
# 인자가 있고 리턴이 없다. => yes in no out
# 인자가 없고 리턴이 있다. => no in yes out
# 인자가 없고 리턴이 없다. => no in no out




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

#1단계! 간단한 문제로 먼저 이해하며 풀어보자!
#1등 선생님 풀이

def am_i_lucky(pick, draw):
    match = set(pick) & set(draw)
    if len(match) == 6:
        return('1등')
    elif len(match) ==5:
        return('3등')
    else: 
        return('꽝') #return이 여러개여도 동시에 실행되지 않음. 하나만 실행됨

result = am_i_lucky([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 7])
print(result)


list_1 = [1, 2, 3, 4, 5, 6]
dict_1 = {
    'numbers': [1, 2, 3, 4, 5, 6],
    'bonus': 7
}



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
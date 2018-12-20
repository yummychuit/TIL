# import random
# import requests
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


import random
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
lotto_data = response.json() #url 받아오기

real_numbers = []
for key, value in lotto_data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)

real_numbers.sort()
bonus_number = [lotto_data['bnusNo']] #로또정보 sort

numbers = list(range(1, 46))
my_numbers = random.sample(numbers, 6)
print('내 번호: ', my_numbers) #로또정보 뽑기


# my_numbers = [1, 2, 3, 4, 5, 6]
# real_numbers = [1, 2, 3, 4, 5, 6]
# bonus_number = [7]

same_numbers = list(set(my_numbers).intersection(real_numbers))
num_same_num = len(same_numbers)
exc_same = list(set(my_numbers).difference(real_numbers))
exc_bonus = list(set(exc_same).intersection(bonus_number))

if num_same_num == 6:
    print("으아항아ㅏ으아앙 1등입니다!!!!!")
elif num_same_num == 5:
    if exc_bonus == []:
        print("오오오옼 3등입니다!!!")
    else:
        print("우와아ㅏㅇ아아 2등입니다!!!!")
elif num_same_num == 4:
    print("우오 4등입니다!!")
elif num_same_num == 3:
    print("오 5등입니다!")
else: print("꽝.....ㅠㅠ")


# while num_same_num

count = 0
for my_number in my_numbers:
    for real_number in real_numbers:
        if my_number == real_number:
            count += 1
print('동일한 숫자 개수: ', count)

if count == 6:
    print(1)
elif count == 5 and bonus in my_numbers:
    print(2)
elif count == 5:
    print(3)
elif count == 4:
    print(4)
elif count == 3:
    print(5)
else : print('꽝')


# list = [1, 2, 3]
# tuple = (1, 2, 3) #list와 tuple이 비슷 
# set = {1, 2, 3} #순서가 없다

my_numbers = set([1, 2, 3, 4, 5, 6]) #set으로 변환
real_numbers = set([1, 2, 3, 4, 5, 6])
bonus_number = 7

match_count = len(my_numbers & real_numbers)
print(match_count)

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


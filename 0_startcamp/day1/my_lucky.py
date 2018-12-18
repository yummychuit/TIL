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




numbers = list(range(1, 46))

my_numbers = random.sample(numbers, 6)

print(my_numbers)

# my_numbers, real_numbers, bonus_number
# 1등 : my_numbers == real_numbers
# 2등 : eal_numbers & my_numbers 가 5개가 같고, 나머지 하나의 my_numbers == bonus_number
# 3등 : real_numbers & my_numbers 가 5개가 같다
# 4등 : real_numbers & my_numbers 가 4개가 같다
# 5등 : real_numbers & my_numbers 가 3개가 같다
# 꽝
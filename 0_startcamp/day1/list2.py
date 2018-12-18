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

n = 0
n = n + 1
n += 1

del(team[6]) #지우기
del(team[2:4])
len(team) #요소가 몇 개인지 확인 가능

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


# 181219 수업정리

## 1.  list & dict 문제풀이

### list 평균 구하기

```python
#1. 평균을 구하시오
my_score = [79, 84, 66, 93]
my_average = sum(my_score) / len(my_score) #float
print(my_average)
```

average함수는 따로 없다!

`len()`은 길이=> 4



### dictionary 평균 구하기

```python
#2. 평균을 구하시오
your_score = {
    '수학': 87,
    '국어': 83,
    '영어': 76,
    '도덕': 100
}
   
your_average = sum(your_score.values()) / len(your_score) #float
print(your_average)

#your_score.values() == [87, 83, 76, 100] #dict_values ??
#print('당신의 평균은:', your_average)
```

`.values()`를 쓰면 value 값



### list in dictionary 평균 구하기

```python
# 문제
cities_temp = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -5, 10],
    '구미': [2, -2, 9]
}

# 3: 도시별 온도 평균
# 서울: ?
# 대전: ?
# 광주: ?
# 구미: ?
```

```python
# 내가 쓴 답
average_seoul = sum(cities_temp['서울']) / len(cities_temp['서울'])
average_dea = sum(cities_temp['대전']) / len(cities_temp['대전'])
average_gwang = sum(cities_temp['광주']) / len(cities_temp['광주'])
average_gu = sum(cities_temp['구미']) / len(cities_temp['구미'])
print('도시별 온도 평균')
print('서울: ', average_seoul,'도')
print('대전: ', average_dea, '도')
print('광주: ', average_gwang, '도')
print('구미: ', average_gu, '도')
```

```python
# 답안1
for city in cities_temp: #for문의 변수?는 키값만 가져옴
    temperatures = cities_temp[city] #그래서 value 가져오기 위해 처리
    avg_temp = round(sum(temperatures) / len(temperatures), 2)
    print(city, avg_temp)

    print(city + ': ' + str(avg_temp)) # 

    print('{0}: {1}'.format(city, avg_temp))
    #str과 함께 써놓은 명령어를 str 말고 명령어로 처리해줘!
```

```python
# 답안2
for key, value in cities_temp.items(): 
#양손으로 둘 다 꺼내요! 왼손은 키, 오른손은 밸류 
#.items() 써야지만 key와 value를 함께 뽑아낼 수 있음 => 리스트같은 거로 바뀌는구나!
    avg_temp = round(sum(value) / len(value), 2) 
    print(key, avg_temp)

    print(key + ': ' + str(avg_temp)) # 
```



### 최대/최소값 구하기

```python
# 문제
cities_temp = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -5, 10],
    '구미': [2, -2, 9]
}
# 4: 도시중에 최근 3일간 가장 추웠던 곳, 가장 더웠던 곳,
# Hottest: ?? , Coldest: ??
```

```python
# 내가 끄적끄적
# value_cities = cities_temp.values()
# value_list = value_cities
#???
# for value_dic in range(0,2):
#     print(value_cities(value_dic))
#???   
# l=[]
# [l.extend([k,v]) for k,v in value_cities.items()]
#???
# a = list(value_cities.items())
#???
# hottest_temp = max(cities_temp.values())
# hottest_reg = 
# print('Hottest: ', )
#???
# for reg in cities_temp:
#???
# reg = cities_temp.keys()
# for reg in cities_temp:
#     print(reg + ': '+ sum)
#???
```

```python
# 답안
# all_temp 모든 기온을 모은다
all_temp = []
for key, value in cities_temp.items():
    all_temp += value

print(all_temp)

# all_temp에서 highest/lowest를 찾는다
highest = max(all_temp)
lowest = min(all_temp)
print(highest, lowest)

# cities_temp에서 highest/lowest가 속한 도시를 찾는다.
hottest = [ ] #dic나 list로 결과가 나오는 것이 좋음. 
coldest = [ ]
for key, value in cities_temp.items(): #서울: [-6, -10, 5]  highest = 10, lowest = -10
    if highest in value:
        hottest.append(key)
    if lowest in value:
        coldest.append(key)

# Hottest: ?? , Coldest: ??
print(hottest, coldest) 
```



## 2. web


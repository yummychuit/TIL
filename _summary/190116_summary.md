# 190116 수업정리

## 1. OOP with Python

- 복습) 01_Python_intro

##### Indexing/Slicing

`[]`를 통한 값 접근 및 `[:]`을 통한 슬라이싱

중간에 있는 틈을 기준으로 생각하면 됨!

l = [ 1, 2, 3, 4, 5 ]
#[ ^, 1, 2, 3, ^ 4, 5 ] 라고 쉼표기준으로 순서를 생각하면 이해하기 쉬움.
l[0:3] # 
l[::-1] #얕은 복사 #[5, 4, 3, 2, 1]
#index넘어가면 오류없이 마지막까지만 잡음
l[::2] #[1, 3, 5]



- 07_OOP

function, class는 선언(정의)하면 바로 object가 생성됨

우리가 이름지어서 담아놓은건 모든 것이 다 객체

class내에서 지정된 것은 기본적으로 담기는 내용이고 나중에 다시 지정해주면 찍혀나옴.. class내의 내용은 온전히 내 것이 아니었음을.....



```python
class Person:
    name = '아이돌'
    
    def greeting(self):
        print(f'hi, my name is {self.name}')
        
p1 = Person()
print(p1.name)
p1.name = 'john'
print(p1.name)
```

-> 인스턴스의 어트리뷰트가 변경되면, 변경된 데이터를 인스턴스 객체 이름 공간에 저장한다.



생성자는 만들어질때, 소멸자는 죽을때!

안쓰면 아무일도 없음. 



```python
def __init__(self, parameter1, parameter2):
    print('생성될 때 자동으로 호출되는 메서드입니다.')
    print(parameter1)

#나는 여러 값을 tuple로 받을거야
def __init__(self, *args):
    print('생성될 때 자동으로 호출되는 메서드입니다.')

#나는 key, value pair를 받을거야
def __init__(self, **kwagrs):
    print('생성될 때 자동으로 호출되는 메서드입니다.')
```



```python
class Person:
    population = 0
    def __init__(self, name):
        self.name = name
        Person.population += 1 #누구의 population인지 명시를 해줘야함
        # 함수 안에서 함수 밖에 있는 애를 수정하려고 하면 안됨
p1 = Person('john')
p2 = Person('tak')
```



static method / class method

```python
class Person:
    population = 0
    def __init__(self, name):
        self.name = name
        Person.population += 1
    def greeting(self):
        print(f'Hi! I am {self.name}')
        
    def show_population():
        print(f'오늘의 인구는 {Person.population}')
    
p = Person('ssafy')
Person.greeting(p)
Person.show_population()
```



call-by-assignment

immutable object

-> int, float, str, tuple

immutable 객체가 함수의 arguments로 전달되면 처음에는 call by reference...



오버라이드 -> 덮어쓰기

세상에 존재하는 연산자의 정의를 사용자가 임의로 정의하여 사용할 수 있음



## 2. module

코드 덩어리 !!

필요한 클래스나 함수를 불러와서 사용하는것

실행하는 파일 입장에서 내가 아닌 다른 파일에서 갖다 쓸 경우 그 파일을 모듈이라고 한다.





## 3. Errors and Exceptions







## 4.


# 1
list, int, str, dict, set

# 2
(5) 숫자 5는 그냥 숫자일 뿐 클래스가 없다.

# 3
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
    
    def greeting(self):
        print(f"'안녕하세요. {self.name}입니다. {self.age}살입니다.'")
    
p1 = Person('홍길동', 20)
p1.greeting()

p2 = Person('둘리')
p2.greeting()
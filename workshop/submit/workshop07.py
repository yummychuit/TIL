# 1
class Circle():
    pi = 3.14
    x = 0
    y = 0
    r = 0
    
    def area(self):
        return self.pi * self.r * self.r
    
    def circumference(self):
        return 2 * self.pi * self.r
    
    def center(self):
        return (self.x, self.y)
    
    def move(self, x, y):
        self.x = x
        self.y = y


cc = Circle()
cc.x = 2
cc.y = 4
cc.r = 3

print(f'넓이는 {round(cc.area(), 2)}이고,')
print(f'둘레는 {cc.circumference()}입니다.')

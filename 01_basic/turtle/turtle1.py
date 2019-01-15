import turtle as t #turtle 너무 기니까 t라고 부를래



class MagicBrush:
    t.color('orange')
    def draw_square(self):
        for i in range(4):
            t.forward(100)
            t.right(90) #방향바꿈

    def draw_triangle(self):
        for i in range(3):
            t.forward(100)
            t.right(120)
    def go(self):
        t.forward(200)

    def turn(self):
        t.right(90)

m1 = MagicBrush() #매직브러쉬 만든다!
m2 = MagicBrush() 

brad = t.Turtle()
brad.shape('turtle')
brad.speed(2)
brad.forward(100)

t.mainloop()
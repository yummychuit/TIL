# 1
def sq_root(x):
    maximum = x
    minimum = 0    
    while 1:
        minimum ** 2 < x < maximum ** 2
        middle_num = (minimum + maximum) / 2
        if round(maximum, 5) == round(minimum, 5):
            return round(maximum, 4)
        elif middle_num ** 2 > x:
            maximum = middle_num
        elif middle_num ** 2 < x:
            minimum = middle_num

sq_root(2)
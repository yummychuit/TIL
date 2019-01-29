# 1
n = 5
m = 9

h = '*' * n
v = ( h + '\n' ) * m

print(v)

# 2
student = { 'python': 80, 'algorithm': 99, 'django': 89, 'flask': 83 }

values = student.values()

print( sum(values) / len(values) )

# 3
blood_type = [ 'A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB' ]

count_a, count_b, count_o, count_ab = 0, 0, 0, 0

for type in blood_type:
    if type == 'A':
        count_a += 1
    elif type == 'B':
        count_b += 1
    elif type == 'O':
        count_o += 1
    elif type == 'AB':
        count_ab += 1

print(count_a, count_b, count_o, count_ab)

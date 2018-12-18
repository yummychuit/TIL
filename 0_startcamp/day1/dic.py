my_info = {
            'name': 'neo',
            'job':'hacker',
            'mobile':'01012345678',
            'email':'neo@hphk.kr'
}

hphk = [
    {
        'name':'john',
        'email':'john@hphk.io'
    },
    {
        'name':'neo',
        'email':'noe@hphk.kr'
    },
    {
        'name':'tak',
        'email':'tak@hphk.io'
    }
]

my_info['email']

type(hphk) #list

p = hphk[2]
type(p) # dict
print(p['name'])
hphk[2]['name']
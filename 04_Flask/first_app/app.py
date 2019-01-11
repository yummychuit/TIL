import random
from flask import Flask ,jsonify # Flask라는 클래스를 빼쓰겠다!

app = Flask(__name__) #type(__name__)은 string / 객체를 생성했다!!

@app.route('/') # @은 decorator ,, .route('/') 는 method를 의미 ,, /뒤에 아무말도 없을때 보통 index 페이지라고 함
def index():
    return 'Hi!'

@app.route('/ssafy') #일반적으로 /뒤에 쓰는 말로 함수이름으로 설정함 ,, 루트 라우팅을 한다고 한다(노선? 하나의 주소에서 여러가지 길이 생기는 것이라 이해하기)
def ssafy():
    return 'sssssssssafy'

@app.route('/pick_lotto')
def pick_lotto():
    numbers = random.sample(range(1, 46), 6)
    return jsonify(numbers)

# @app.route('/hi/kmj') #/뒤에 있는 이름을 정확하게 써줘야 동작함
# def hi():
#     return(f'hi kmj!')

@app.route('/hi/<string:name>') #<>안의 값은 변수
def hi(name):
    return(f'hi {name}!')


@app.route('/dictionary/<string:word>')
def my_dictionary(word):
    my_dic = {
        'apple': '사과',
        'banana': '바나나',
        'melon': '멜론',
        'cherry': '체리',
        'grapefruit': '자몽',
        'pomegranate': '석류'
    }

    if word in my_dic:
        return f'{word}은(는) {my_dic[word]}!!'
    else:
        return f'{word}은(는) 나만의 단어장에 없는 단어입니다!'

if __name__ == '__main__':   #run -> 서버가 돌고있다! <-> 서버가 죽었다ㅠㅠ
    app.run(debug=True) # **kwagrs 사용하여 입력된듯





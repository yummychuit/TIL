# 1
from flask import Flask

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
# 파일명 변경 금지
# 아래에 클래스 Word를 선언하세요.
class Word:
    wordbook = {}

    def add(self, 영문, 한글):
        Word.wordbook[영문] = 한글

    def delete(self, 영문):
        if 영문 not in Word.wordbook.keys():
            return False
        else:
            Word.wordbook.delete(영문)
            return True
    
    def print(self):
        for key, value in Word.wordbook.items():
            print(key, value)




# 아래의 코드는 수정하지마세요. 
if __name__ == '__main__':
    my_book = Word()
    my_book.add('apple', '사과')
    my_book.add('banana', '바나나')
    my_book.add('cherry', '체리')
    my_book.add('durian', '두리안')
    my_book.print() 
    print(my_book.delete('cherry'))
    print(my_book.delete('durian'))
    print(my_book.delete('egg'))
    my_book.print()
    my_book.print()
    my_book.add('egg', '계란')
    my_book.print()


#풀이
class Word:
    def __init__(self):
        self.wordbook = {}

    def add(self, eng, kor):
        self.wordbook[eng] = kor

    def delete(self, eng):
        if eng in self.wordbook:
            self.wordbook.pop(eng)
            return True
        else:
            print('No such word')
            return False

    def print(self):
        for key, value in self.wordbook.items():
            print(f'{key}: {value}')
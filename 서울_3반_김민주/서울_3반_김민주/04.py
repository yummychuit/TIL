# 파일명 변경 금지
def cipher(word, n):
    # 아래에 코드를 작성하시오.
    # word는 모두 소문자로만 구성되어 있습니다.
    # n은 양의 정수입니다.
    # 암호화된 문자열을 반환합니다.
    
    new_word = []
    for text in word:
        new_int = ord(text) + n
        if new_int > 122:
            new_int = new_int - 26
        else:
            new_int = new_int
        new_text = chr(new_int)
        new_word.append(new_text)
    return ''.join(new_word)



# 아래의 코드는 수정하지마세요. 
if __name__ == '__main__':
    print(cipher('apple', 1))
    print(cipher('apple', 27))
    print(cipher('zoo', 2))
    print(cipher('queen', 16))
    print(cipher('queen', 100))


#풀이
def cipher(word, n):
    result = ''
    for char in word:
        if ord(char) + n % 26 > 122:
            result += chr(ord(char) + n % 26 - 26)
        else:
            result += chr(ord(char) + n % 26)

    return result
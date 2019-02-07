# 파일명 변경 금지
def alphabet_count(word):
    # 아래에 코드를 작성하시오.
    # word는 소문자로만 구성 되어있습니다.
    # 딕셔너리를 반환합니다.

    dict_alpha = {}
    alphabet = []
    for alpha in word:
        if alpha not in alphabet: 
            alphabet.append(alpha)
            dict_alpha[alpha] = word.count(alpha)
    return dict_alpha



# 아래의 코드는 수정하지마세요. 
if __name__ == '__main__':
    print(alphabet_count('hello'))
    print(alphabet_count('internationalization'))
    print(alphabet_count('haha'))
    print(alphabet_count('computer'))
    print(alphabet_count('yoyo'))

#풀이
def alphabet_count(word):
    result = {}
    for char in word:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
        return result
# 파일명 변경 금지
def alphabet_mode(word):
    # 아래에 코드를 작성하시오.
    # word는 소문자로만 구성 되어있습니다.
    # word에서 가장 많이 발생한 알파벳 하나를 반환합니다.
    
    if len(word) > 1:
        if word[0] != word[1]:
            if word.count(word[0]) >= word.count(word[1]):
                word = word.replace(word[1],'')
                ''.join(word)
            else: 
                word = word.replace(word[0],'')
                ''.join(word)
            return alphabet_mode(word)
        else:
            # word[1]을 다시 word[0]으로 하고 word[2]를 word[1]로 두고싶었는데요...
    else:
        return word

# 중복되지 않는 알파벳만 뽑아서 key로 하고 count를 value로 한 뒤에 value가 가장 큰 key값을 뽑아내는 방법..을 하고싶었어요...

# 아래의 코드는 수정하지마세요. 
if __name__ == '__main__':
    print(alphabet_mode('hello'))
    print(alphabet_mode('internationalization'))
    print(alphabet_mode('haha'))
    print(alphabet_mode('computer'))
    print(alphabet_mode('yoyo'))


#풀이
def alphabet_mode(word):
    result = {}
    for char in word:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    for key, value in result.items():
        if (max(result.values()) == value):
            return key
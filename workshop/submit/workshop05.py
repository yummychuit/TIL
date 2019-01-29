# 1
def palindrome(word):
    rev_word = word[::-1]
    if word == rev_word:
        return True
    else:
        return False
    
print(palindrome('a'))
print(palindrome('nan'))
print(palindrome('토마토'))

# 2
def palindrome(words):
    fir_word = words.lower()
    sec_word = []
    for word in fir_word:
        if word != ' ':
            sec_word.append(word.strip())
        else:
            pass
    
    rev_words = sec_word[::-1]
    if sec_word == rev_words:
        return True
    else:
        return False

print(palindrome('A Santa at NASA'))
